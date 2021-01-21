## React State Management 종류
  
https://areknawo.com/top-5-react-state-management-libraries-in-late-2020/  
  
* Redux
* MobX
* Recoil
* Akita
* Hookstate

State 관리 라이브러리가 꼭 필요한 것은 아니다. 기본 제공 State, Context APIs로도 해결이 가능하다. 너무 복잡하지만 않다면.  

## 그렇다면 Context API 라는건 무엇일까?
`Context is designed to share data that can be considered “global” for a tree of React components, such as the current authenticated user, theme, or preferred language. For example, in the code below we manually thread through a “theme” prop in order to style the Button component:`  
전역으로 사용되는 것들, 예를 들면 테마 설정등에 쓰인다.

### Context API를 사용하기 전에
다른 레벨의 컴포넌트들에서 많이 사용해야할 때만 사용하는 것을 추천한다.  즉, 로그인과 같은 '상태 저장'과는 거리가 있다.  

## Redux vs MobX
둘 다 State 관리 라이브러리라는 점에서 비슷하지만, MobX가 좀 더 '관찰 가능한 접근'에서 장점이 있고,
Redux, MobX 모두 학습 곡선이 가파르다는 단점이 있지만, 학습을 모두 완료했을 때에 MobX는 매우 강력하고 덜 반복적
이라는 장점이 있다. 그러나 MobX는 결코 가벼운 라이브러리가 아니다. 미니멀리스트들에게는 추천되지 않는 라이브러리이다.
