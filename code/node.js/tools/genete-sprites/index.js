
const exec = require('child_process').exec
// npm install --save-dev images
// npm install --save-dev get-pixels
const imageResizeCmdStr = 'node image-resize.js'
// npm install gka -g
const spriteGeneratorCmdStr = 'node sprite-generator.js'

console.log(imageResizeCmdStr)
exec(imageResizeCmdStr, function(err, stdout, stderr) {
  if (err) {
    console.log(err)
  } else {
    stdout && console.log(stdout)
    console.log(spriteGeneratorCmdStr)
    exec(spriteGeneratorCmdStr, function(err, stdout, stderr) {
      err && console.log(err)
      stdout && console.log(stdout)
    })
  }
})
