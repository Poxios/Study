https://hello-bryan.tistory.com/134

* .env.development
* .env.production

root에 다음과 같은 파일들을 만들어준다.  
CRA (Create-React-App)으로 생성된 프로젝트인 경우  
REACT_APP_API_HOST="https://dev-api.banchangohub.com/v3/"  
이런식으로 앞에 REACT_APP을 붙여줘야 한다.
  
보통 치면 나오는거는 다 npm start시에 변수를 설정하는거다. 실제로는 npm build에서 작동되어야한다.
https://engineering.huiseoul.com/react-prod-staging-dev-%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0-8eb6bbccddfe  
  
그리고 이거는 진짜 CRA
https://m.blog.naver.com/legend25/222033372402  

```js
"scripts": {
    "start": "react-scripts start",
    "build": "env-cmd -f .env react-scripts  build",
    "build:prod": "env-cmd -f .env.production react-scripts  build && move build ./build_prod",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
```
