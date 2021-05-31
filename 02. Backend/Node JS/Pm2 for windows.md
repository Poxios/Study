# 프로세스 관리자 (프로젝트 관리자) PM2를 윈도우에서 실행
* 윈도우에서는 PM2가 실행이 잘 되지 않는다.
* 이 때, 우회적인 방법으로 바로 `index.ts`를 실행하는 것이 아니고 `startscript.js`를 만들어서 이것을 실행한다.
```js
// startscript.js
const exec = require("child_process").exec;
const path = require("path");
const client = exec("npm start", {
  windowsHide: true,
  cwd: path.join(__dirname, "./"),
});
client.stdout.pipe(process.stdout);
client.stderr.pipe(process.stderr);
```
* https://ordinary-code.tistory.com/67
