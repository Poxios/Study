### 원본 커밋 Timestamp를 보존하면서 폴더 이름 바꾸기
0. Verified 마크 달아라.
1. 기존에 있는 모든 파일에 대한 Timestamp, commit message를 DB화 해놓는다.
2. 변경된 File Structure은 로컬에만 저장해둔다.
3. 모든 단일 파일에 대해서 커밋을 수행한다. 단, DB에서 불러온 시간을 기준으로 커밋한다. (커밋 시간 내림차순 기준.) Timestamp가 완전히 동일한건 묶어서 커밋을 수행한다.

01. Frontend
02. Backend
03. Security
04. 

예를 들어 

original | timestamp | target file
NodeJS/asdf.md | 20200220 | FrontEnd/NodeJS/asdf.md 

---
TODO: Algorithm Study 여기에 병합하기. Timestamp도 보존하면서.