https://www.smashingmagazine.com/2020/08/comment-system-firebase/
  
맨 밑에 DB 보안땜에 써놓음
  
## Firebase Functions onCall이 없는 보안 로그인 통신 - 토큰 
https://firebase.google.com/docs/auth/admin/verify-id-tokens?hl=ko
  
## 토큰 재인증 - 클라이언트 사이드에서
https://firebase.google.com/docs/auth/admin/manage-sessions?hl=ko#detect_id_token_revocation
![image](https://user-images.githubusercontent.com/62606632/106087944-5970f480-6168-11eb-9aab-481a47f856a3.png)
![image](https://user-images.githubusercontent.com/62606632/106087803-1878e000-6168-11eb-8c5f-21e541d41693.png)
  
## Firebase 사용시 JS 사용 문법 플로우
![image](https://user-images.githubusercontent.com/62606632/106088493-680bdb80-6169-11eb-8329-b7589d1b982e.png)
  
## Firebase .env 적용
```js
admin.initializeApp({
  credential: admin.credential.cert({
      projectId: process.env.FIREBASE_PROJECT_ID, // I get no error here
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL, // I get no error here
      privateKey: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, '\n') // NOW THIS WORKS!!!
  }),
  databaseURL: process.env.FIREBASE_DATABASE_URL
});
```  
replace()가 있어야한다.
