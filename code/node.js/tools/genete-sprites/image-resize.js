const images = require('images')
const { delFile } = require('./utils')
const fs = require('fs')
// 目录结构
// target/
//   dir1
//   dir2
//   dir3
//   ...
const targetPath = 'target'
const distPath = 'dist'
// 电脑有, 16384
// 手机有, 4096
const maxWidth = 4096
// 256 会太糊
const resizeWidth = 512
const quality = 100

if (!fs.existsSync(distPath)) {
  fs.mkdirSync(distPath)
} else {
  delFile(distPath, distPath)
}

fs.readdir(targetPath, function (err, dirs) {
  for (let i = 0; i < dirs.length; i++) {
    let targetDir = `${targetPath}/${dirs[i]}`
    // let files = fs.readdirSync(targetDir)
    // for (let i = 0; i < files.length; i++) {
    //   let filename = `${targetDir}/${files[i]}`;
    //   let fileConpArr = filename.split('-');
    //   let rename = `${fileConpArr[0]}-${fileConpArr[1].padStart(7, '0')}`
    //   fs.renameSync(filename, rename);
    // }

    let distDir = `${distPath}/${dirs[i]}`
    if (!fs.existsSync(distDir)) {
      fs.mkdirSync(distDir)
    }

    files = fs.readdirSync(targetDir)
    for (let i = 0; i < files.length; i++) {
      const dist = `${distDir}/${Math.floor(i / 128)}`
      
      if (!fs.existsSync(dist)) {
        fs.mkdirSync(dist)
      }
      
      if (i % 2) { continue }
      // fs.renameSync(`${targetDir}/${files[i]}`, `${dist}/${files[i]}`);
      images(`${targetDir}/${files[i]}`)
        .resize(resizeWidth)
        .save(`${dist}/${files[i]}`, {
          quality
        })
    }
  }
})
