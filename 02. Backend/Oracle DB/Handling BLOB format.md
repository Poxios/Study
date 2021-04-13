# LOB 형식 처리하기
## BLOB
* Golden과 같은 뷰어에서는 그대로 텍스트 형식으로 읽히지만, 형식이 BLOB라서 JS같은 곳에서 읽어올 때에 Raw 형식으로 읽히는 문제가 발생했다.
```sql
SELECT DBMS_LOB.SUBSTR(컬럼명, 4000, 1) FROM 테이블명;
```
이런 식으로 해도 되고,
```sql
SELECT  DBMS_LOB.SUBSTR(CONTENTS, DBMS_LOB.GETLENGTH(CONTENTS), 1) AS LOB_CONTENTS
  FROM  TB_FOO
```
이런 식으로 해도 된다. `DBMS_LOB.SUBSTR`이 가장 중요하다.
```sql
DBMS_LOB.INSTR(CONTENTS, 'Cookie', 1, 1) > 0
```
이런 것도 있다. 추후 학습 요망.
