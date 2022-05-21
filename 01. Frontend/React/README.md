# 리액트 개발시 필독
* 작업관리자에서 리액트 Dev 웹서버 (Node) 우선순위 매우 높음으로 하면 컴파일시 속도 매우 빨라짐!

# 이외
* 2021 05 05에 생성한 왜 Unused vars가 안좋은가.md 파일 이름에 특수문자 '?' 사용해버려서 특정 두 커밋에는 윈도우 환경에서 접근 안됨. 추후 수정 필요.

## 다음 개발에 필수적으로 고려되어야 할 사항들
* Material ui - Global Theme 적용으로 일괄 테마 적용 및 모든 Styled Component들을 Material Ui - makeStyle로 적용. (Use Ref의 장단점도 조사)
* Material ui - Backdrop Loading Process를 Context에 적용해서 isBusy를 글로벌하게 사용할 수 있게 적용. 특히 이 방법을 사용하면 isBusy로 Component들을 Disabled 처리하지 않아도 사용자로부터 입력을 제한할 수 있음. 특히 중요한 것은 중첩된 async - await문인데, 이를 처리하기 위해서 `class LoadingManager()`를 설정하고, LoadingManager에 해당하는 `Stack`(Static Type. 생성자를 Private)을 만들어서 처리하자. `push`, `pop`을 수행할 수 있게. 다만, `history.push`와 같은 작업들 때문에 제대로 `pop()`처리가 안된 경우, 어디서 그런 문제가 나타나는지 확실하게 핸들링 해야한다.
* 자꾸 `may cause memory leak`나오는 오류 어디서 나오는건지 보자. 바로 위의 Loading State 관리에 악영향을 줄 수 있다.
* 모든 Async - Await 과정에 Error Handling을 명확히 적용. 오류 정보들을 묶어서 보낼 수 있게 적용하는 것도 고려. 사용자에게 허락 받아야하는지도 조사.
* 2022 04 25 Added. NEED TO SEND ERROR SITUATION INFO TO SERVER. IT NEEDS TO BE NOTIFIED TO USER? EX) ALL FRONT ERROR - DO IT IN TRY, CATCH BLOCK - TO BACKEND ERROR LOGGER API
### Vite 사용하기
* create-react-app 대신 Vite를 사용해야한다!