## 사용법
가입 후, 앱 생성 후 Github Actions 연동. 이후에는 Node js 서버 돌리면 된다.

## 세팅 해줘야 할 것
```js
const express = require("express");
const app = express();
const PORT = process.env.PORT;

function handleListening() {
  console.log(`Listening on: http://localhost:${PORT}`);
}
function handleHome(req, res) {
  res.send("hello");
}

app.get("/", handleHome);

app.listen(PORT, handleListening);

```

PORT 설정 조심해야함.

```json
{
  "name": "",
  "version": "1.0.0",
  "description": "Backend",
  "main": "index.js",
  "repository": "https://github.com",
  "author": "Poxios <poxios0310@gmail.com>",
  "license": "MIT",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "engines":{
    "node": "v15.1.0",
    "npm": "7.0.8"
  }
}

```

node -v / npm -v로 버전 넣어줘야함. 헤로쿠는 해야한다고 한다.

## Sleep 안들게 하기
`http://kaffeine.herokuapp.com/` 여기에 도메인 등록하면 카페인 샷 넣어줌. 6시간 수면시간 넣어줘야함.
