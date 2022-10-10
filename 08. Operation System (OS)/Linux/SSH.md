## With Oracle Free Tier
* `chmod 0400 ./ssh-key.key` - ssh에 사용되는 시크릿 키는 모두가 볼 수 있으면 안된다.
* `ssh -i ./ssh-key.key opc@000.000.000.000` - private키로 ssh 연결
* `sudo passwd root` - root 비번 초기화