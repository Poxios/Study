https://hello-bryan.tistory.com/134

* .env.development
* .env.production

root에 다음과 같은 파일들을 만들어준다.  
CRA (Create-React-App)으로 생성된 프로젝트인 경우  
REACT_APP_API_HOST="https://dev-api.banchangohub.com/v3/"  
이런식으로 앞에 REACT_APP을 붙여줘야 한다.
  
보통 치면 나오는거는 다 npm start시에 변수를 설정하는거다. 실제로는 npm build에서 작동되어야한다.
