# DB Folder 옮기는 법
1. MongoDB 설치 폴더의 data 폴더가 DB 정보들을 담고 있는 폴더이다.
2. 백그라운드에 `mongo.exe`, `mongod.exe`가 모두 꺼져있는지 확인 후에, 해당 `data` 폴더를 복사해서 옮긴다.
3. mongod.exe가 강제로 꺼졌으면 `mongod -f mongod.cfg`를 통해 켜야한다. 이 때 콘솔에 아무 일도 일어나지 않는 것이 정상이다.
