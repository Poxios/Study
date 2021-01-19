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

## a 페이지에서 b 페이지로 이동하면서 값을 전달하고 싶을 때:
```js
// a.tsx 
import { useHistory } from 'react-router-dom';
...

const history = useHistory();
history.push({
            pathname: '/otp/check',
            search: '?query=abc',
            state: { isOTP: isOTP },
          });
===

//b.tsx
import { useHistory, useLocation } from 'react-router-dom';
...

const location = useLocation();
console.log(location.state);
```

## useState, useCallback 정리
```js
const getApi = useCallback(async () => {
    warehouseApi	    warehouseApi
      .getByMainItemTypes(clickedItems, 0, 10)	      .getByMainItemTypes(clickedItems, pageIndex, 10)
      .then(({ data: { warehouses } }) => {	      .then(({ data: { warehouses } }) => {
        setResults(warehouses);	        if (isExtraLoading) {
          setResults((prevResults) => [...prevResults, ...warehouses]);
        } else {
          setResults(warehouses);
        }
        setLoading(false);
      })	      })
      .catch(({ response: { status } }) => {	      .catch(({ response: { status } }) => {
        if (status === 404) {	        if (status === 404) {
          message.warning('검색 결과가 존재하지 않습니다.');	          if (isExtraLoading) {
            message.warning('더 이상 검색 결과가 없습니다.');
          } else {
            message.warning('검색 결과가 존재하지 않습니다.');
          }
        } else {
        }	        }
        setLoading(false);
      });	      });
  }, [clickedItems]);	  }, [clickedItems, pageIndex, isExtraLoading, setResults]);

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
하면 되는줄 알았으나 router v5.0부터는
https://raptis.wtf/blog/custom-hook-to-connect-google-analytics-in-react/  
이거 

```js
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import ReactGA from 'react-ga';

const UseGoogleAnalytics = () => {
  const location = useLocation();

  useEffect(() => {
    ReactGA.initialize('UA-xxx');
  }, []);

  useEffect(() => {
    const currentPath = location.pathname + location.search;
    ReactGA.set({ page: currentPath });
    ReactGA.pageview(currentPath);
  }, [location]);
};
export default UseGoogleAnalytics;

```  
그리고 Router에서
```js

const RouterComponent = () => {
  UseGoogleAnalytics();
  return (
    <Switch>
      <Route path="/" exact component={Main} />
      <Route path="/login">
      
  .....
  
  
const RouterExporter = () => {
  return (
    <Router>
      <RouterComponent />
    </Router>
  );
};
```
