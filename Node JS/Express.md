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
