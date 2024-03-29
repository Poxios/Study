## 라우터
```js
// birds.js
var express = require('express');
var router = express.Router();

// middleware that is specific to this router
router.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
});
// define the home page route
router.get('/', function(req, res) {
  res.send('Birds home page');
});
// define the about route
router.get('/about', function(req, res) {
  res.send('About birds');
});

module.exports = router;
```  
이후 이런 식으로 불러오면 된다. 이러면 timestmap 기능이 있는 라우터가 되는거다.
```js
var birds = require('./birds');
...
app.use('/birds', birds);
```
  
## 에러 핸들링
```js
var bodyParser = require('body-parser');
var methodOverride = require('method-override');

app.use(bodyParser());
app.use(methodOverride());
app.use(function(err, req, res, next) {
  // logic
});
```
무조건 인자를 4개 가져야한다. 그렇지 않으면 일반적인 미들웨어로 인식할 것이다.  
  
이런식으로 throw Error 사용.
```js
const app = require("express")()

app.get("*", function (req, res, next) {
  // 비동기 오류를 보고하려면 반드시 next()를 통과해야 합니다
  setImmediate(() => {
    next(new Error("woops"))
  })
})

app.use(function (error, req, res, next) {
  // 여기에 도달할 것입니다
  res.json({ message: error.message })
})

app.listen(3000)
```  
  
express의 비동기 처리는 그지같다. 2011 ~ 2014년에 대부분 짜여졌기 때문이다.  
```js
function wrapAsync(fn) {
  return function (req, res, next) {
    // 모든 오류를 .catch() 처리하고 체인의 next() 미들웨어에 전달하세요
    // (이 경우에는 오류 처리기)
    fn(req, res, next).catch(next)
  }
}
```
를 사용하면 된다. 
  
클라이언트 오류는 400, 서버 오류는 500을 주고싶다면?
```js

const { AssertionError } = require("assert")
const { MongoError } = require("mongodb")

app.use(function handleAssertionError(error, req, res, next) {
  if (error instanceof AssertionError) {
    res.status(400).json({
      type: "AssertionError",
      message: error.message,
    })
  }
  next(error)
})

app.use(function handleDatabaseError(error, req, res, next) {
  if (error instanceof MongoError) {
    res.status(503).json({
      type: "MongoError",
      message: error.message,
    })
  }
  next(error)
})
```
## 로깅
morgan, winston 쓰는데 콘솔에 찍을거면 morgan쓰면 된다.

## 비동기 처리
* https://programmingsummaries.tistory.com/399
* https://thewavelet.tistory.com/40
* 기본적으로 express는 비동기 처리를 지원하지 않는다. 정확히는 비동기를 지원하지 않는게 아니고, **기존에 구동 중 Error 발생 시 자동으로 Next Function이 실행되었던 것이 Promise Rejection과 호환되지 않아서 Next Function으로 넘어가지 않는 것이다.**

## Middleware & Typescript
* 간혹 Request에 유저 정보라든지에 대한 새로운 필드를 추가하여 사용해야할 때가 있다.
* 이럴 때 d.ts를 사용해야한다.
* https://wooooooak.github.io/node.js/2018/12/18/express%EC%99%80-Typescript-%EC%82%AC%EC%9A%A9-%EC%A4%91-req%EC%97%90-%EC%9E%84%EC%9D%98%EC%9D%98-%EA%B0%92-%EB%84%A3%EA%B8%B0/
