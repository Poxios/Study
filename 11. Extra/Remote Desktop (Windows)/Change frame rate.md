# RDP에서 프레임 바꾸기 (기본30)
## Group Policy
1. 관리 템플릿 -> Windows 구성 요소 -> 터미널 서비스 -> 원격 데스크톱 세션 호스트 -> 원격 세션 환경 -> 원격 데스크톱 연결에 H.265/AVC444 그래픽 모드 우선 사용 설정

## 레지스트리
1. 컴퓨터\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations
2. DWMFRAMEINTERVAL를 32비트로 생성
3. 16진수 -> "f"를 넣어준다.
4. 서비스 -> Remote Desktop 서비스 재시작.