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

# React-GA
## 설치법
`yarn add react-ga`  
  
## 적용법
App.js에서 import 후
```js
componentDidMount = () => {
    ReactGA.initialize('UA-187568714-1');
    ReactGA.pageview(window.location.pathname + window.location.search);
};
```  
하면 됨.
