## VSCode를 위한 C / C++ 기본 환경
* .vscode 안에는 디버깅을 위한 세팅이 들어있습니다.
* WSL 설치 후 실행 전, 다음과 같은 세팅이 선행되어야 합니다.
```shell
sudo apt update
sudo apt upgrade
sudo apt install gcc
sudo apt install g++
sudo apt install gdb
```
* .clang-format 안에는 bracket 세팅에 대한 정보들이 들어있습니다.