# 리액트 개발시 필독
* 작업관리자에서 리액트 Dev 웹서버 (Node) 우선순위 매우 높음으로 하면 컴파일시 속도 매우 빨라짐!

# 이외
* 2021 05 05에 생성한 왜 Unused vars가 안좋은가.md 파일 이름에 특수문자 '?' 사용해버려서 특정 두 커밋에는 윈도우 환경에서 접근 안됨. 추후 수정 필요.

## 다음 개발에 필수적으로 고려되어야 할 사항들
* Material ui - Global Theme 적용으로 일괄 테마 적용 및 모든 Styled Component들을 Material Ui - makeStyle로 적용. (Use Ref의 장단점도 조사)
* Material ui - Backdrop Loading Process를 Context에 적용해서 isBusy를 글로벌하게 사용할 수 있게 적용.
* 모든 Async - Await 과정에 Error Handling을 명확히 적용. 오류 정보들을 묶어서 보낼 수 있게 적용하는 것도 고려. 사용자에게 허락 받아야하는지도 조사.
