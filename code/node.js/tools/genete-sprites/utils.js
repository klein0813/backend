const getPixels = require("get-pixels")
const fs = require('fs')
const path = require('path')

function delFile(path, reservePath) {
  if (fs.existsSync(path)) {
    if (fs.statSync(path).isDirectory()) {
      let files = fs.readdirSync(path)
      files.forEach((file, index) => {
        let currentPath = path + "/" + file
        if (fs.statSync(currentPath).isDirectory()) {
          delFile(currentPath, reservePath)
        } else {
          fs.unlinkSync(currentPath)
        }
      })
      if (path != reservePath) {
        fs.rmdirSync(path)
      }
    } else {
      fs.unlinkSync(path)
    }
  }
}

function getImagePixels (imgPath) {
  getPixels(imgPath, function(err, pixels) {
    if(err) {
      console.log("Bad image path")
      return
    }
    const width = pixels.shape[0]
    const height = pixels.shape[1]
    const dataMatrix = new Array(width * height).fill(0)
    const { data } = pixels
    let c = 0
    for (let i = 0; i < data.length; i += pixels.shape[2]) {
      const r = data[i]
      const g = data[i + 1]
      const b = data[i + 2]
      const dx = r - 255
      const dy = g - 255
      const dz = b - 0
      if ((r - b) >= 50 && (g - b) >= 50 || dx * dx + dy * dy + dz * dz < 5000) {
        dataMatrix[c] = 1
      }
      c++
    }
    let file = path.resolve(__dirname, './file.txt')
    fs.writeFile(file, dataMatrix.toString(), { encoding: 'utf8' }, err => {})
  })
}

module.exports = {
  delFile,
  getImagePixels
}
