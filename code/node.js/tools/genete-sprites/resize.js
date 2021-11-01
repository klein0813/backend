const images = require('images')
const fs = require('fs')

const files = fs.readdirSync('./dist/combine')
for (let i = 0; i < files.length; i++) {
  const dist = './dist-resize'
  if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
  }
  images(`./dist/combine/${files[i]}`)
    .resize(4096)
    .save(`${dist}/${files[i]}`, {
      quality: 100
    })
}