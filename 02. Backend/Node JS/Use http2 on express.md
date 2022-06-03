# Use http2 on express
* Cert files required
```js
const express = require('express')
const http2Express = require('http2-express-bridge') // <-- important
const http2 = require('http2')
const { readFileSync } = require('fs')
// only change required
const app = http2Express(express)

app.get('/express', (req, res) => {
  res.send('Hello World');
})
const options = {
  key: readFileSync('<Certificate Key>'),
  cert: readFileSync('<Certificate file>'),
  allowHTTP1: true
}
const server = http2.createSecureServer(options, app)
server.listen(3000)
```