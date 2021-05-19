# useMemo, useCallback은 언제 써야할까?

- useMemo는 상수 정의, useCallback은 함수 정의를 할 때 사용한다고 알고 있다.
- 그런데, 우리가 평소에 React Component 범위 밖에 정의하는 상수들을 끌어다 쓰는 것과 어떤게 다를까?
- 가장 큰 차이는 다른 변수들에 의해 값이 영향 받을 때, 유연하게 상수를 정의할 수 있다는 것이다.
- 예를 들어, Axios GET 요청을 Auth에 대한 정보가 담긴 Header와 함께 보내야한다고 가정해보자.
- 이때, 본인의 Bearer Token이 담긴 Header을 함께 묶어서 Axios Instance로 정의하고 싶다면, 본인의 Token 값을 Redux든 Context든 어딘가에서 받아와야 한다.
- Redux Container에서든 Context에서든 정보를 받아오기 위해서는 React Component 내부에 존재해야 그것이 가능하다. 따라서 이럴 때 useMemo, useCallback을 사용한다.
- 또한, 두 기능에 모두 존재하는 Dependencies Array 등록을 통해 불필요한 재정의를 방지할 수 있다.
