https://medium.com/@trustyoo86/async-await%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-loop-%EB%B3%91%EB%A0%AC%EB%A1%9C-%EC%88%9C%EC%B0%A8-%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0-315f31b72ccc
```js
 await Promise.all(
        commentsArr.map(async (doc, idx) => {
          if (doc.subCommentsExist) {
            await db
              .collection("departMajor")
              .doc(docId)
              .collection("comments")
              .doc(doc.commentId)
              .collection("subcomments")
              .orderBy("timestamp")
              .get()
              .then((querySnapshot) => {
                querySnapshot.forEach((doc) => {
                  let data = doc.data();
                  let distanceText = formatDistanceToNow(
                    data.timestamp.toMillis(),
                    {
                      locale: ko,
                    }
                  ).replace("약 ", "");
                  if (distanceText.includes("미만")) {
                    distanceText = "방금";
                  }
                  commentsArr[idx].subComments.push({
                    subcommentId: doc.id,
                    content: data.content,
                    timestampDistance: distanceText,
                    timestampMillis: data.timestamp.toMillis(),
                    likeCount: data.likes_count,
                  });
                });
              });
          }
        })
      );
```
forEach(async ()=>{}) 이런식이면 내부의 익명함수들이 다 실행되기 전에 넘어가버린다.  
forEach 앞에다가 await을 붙인다고 해결되는게 아닌데, 이거는 위에 Promise.all로 해결 가능.
병렬 실행인것이다. 직렬로 하고 싶으면 (순서가 중요하면) for ( a of b ) 로 하면 된다!
