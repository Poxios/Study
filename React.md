## 스크롤 이벤트 등록법
```js
 const onScroll = () => {	
    const refBottom = document	
      .getElementById('RefsWrap')	
      .getBoundingClientRect().bottom;	
    if (refBottom < 0) {	
      setIsTop(true);	
    }	
  };	
  useEffect(() => {	
    window.addEventListener('scroll', onScroll);	
    return () => window.removeEventListener('scroll', onScroll);	
  }, []);
```

## 하단 경계선을 넘었을 때 계산법
```js
 const refBottom =
        document.getElementById('RefsWrap').getBoundingClientRect().bottom -
        window.innerHeight;
```
