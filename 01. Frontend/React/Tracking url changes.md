https://help.mouseflow.com/en/articles/4310818-tracking-url-changes-with-react
```js
import React, { useEffect } from 'react' 
import App from './components/App' 

import { useHistory } from 'react-router-dom' const 

Root = () => { 
   const history = useHistory() 

   useEffect(() => {
      return history.listen((location) => { 
         console.log(`You changed the page to: ${location.pathname}`) 
      }) 
   },[history]) 

   return ( 
      <App /> 
   ) 
}
```
