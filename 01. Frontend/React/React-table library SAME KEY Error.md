## 문제 상황
* react table로 작업을 하고 있는데 갑자기 언제부터인가 계속 same key error이 났다.
## 접근법
* 모든 행, 열, 셀에 대해서 key를 console.log 찍어보았다.
* 결국 footer 쪽에 문제가 있다는 것을 알아냈다
## 해결법
* All이 문제였다.
```js
rowsPerPageOptions={[
                  5,
                  10,
                  15,
                  25,
                  { label: "All", value: data.length },
                ]}
```
* 다음과 같은 구문이 TablePagination에 있었는데, All의 value인 `data.length`이 문제였다.
* 만약 전체 데이터 개수가 5, 10, 15, 25개 중 하나이면, Key도 그것과 겹쳐서 일어나는 문제였다.
* All을 제거하거나, 이에 해당하는 개수와 충돌하지 않도록 예외를 잘 처리해주면 된다.
