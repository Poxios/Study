## apt update / upgrade 에러 해결
* apt update 또는 upgrade를 실행하면 우분투 서버와 연결에 실패하는 오류이다.
* 다음과 같이 구글 DNS로 바꿔주면 해결된다.
```console
echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null
apt update
apt upgrade
```