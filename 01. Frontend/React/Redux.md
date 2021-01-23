https://redux.js.org/tutorials/essentials/part-1-overview-concepts
# Redux Essentials
## Redux는 무엇이고, 언제쓰이는가?
`Redux is a pattern and library for managing and updating application state, using events called "actions". It serves as a centralized store for state that needs to be used across your entire application, with rules ensuring that the state can only be updated in a predictable fashion.`  
프로젝트 전체를 관통하는, 중앙 상태 저장소 역할을 한다. 예측 가능한 상황에서 업데이트 되어야 하는 조건이 붙는다.  
리덕스에는 장단점이 존재한다.  
*__단점__: 배워야할게 많고, 더 많은 코드들을 작성해야한다. 코드에 간접적인 것들을 추가해야하고, 몇 가지 제한 사항이 붙는다. 장기 생산성과, 단기 생산성의
교환이라고 생각하면 된다.
*__장점__: 앱 상에서, 많은 곳에서 동일한 state에 접근해야 할 때에 좋고, 자주 변경되는 state에 접근해야할 때에도 좋다. 많은 사람들이 관리하는 코드에서도 
가독성을 높여준다.

## State 관리
`One way data flow`의 상황일때에는, 기존 state 관리의 방법이 불편하지 않다. 그러나 많은 컴포넌트에서 동시에 접근해야 하는 상황에서, 불편해진다.

## 불변성 (Immutability)
코드에서 불변성이란, Object, Array와 같은 것들의 값이 변경되기 위해서 따로 copy할 변수를 만들어서 옮겨야 하는 것을 말한다. 즉, 직접 
변수에 접근해 바꿀 수 없다는 것이다. Redux 또한 이 특징을 가지고있다.  

## 용어 설명
* Actions: 앱에서 무언가 일어났다고 보면 된다.
* Actions Creators: action object를 만들거나 반환하는 함수를 가리킨디. 이것을 사용함으로써 우리는 매번 action object를 작성하지 않아도 된다.
* Reducer: 현재 state와 action object를 수신하는 함수이다. 필요하다면 수신 후 변경까지 담당한다. 수신된 action 타입에 따라서 작동하는 
event handler로 생각하면 좋다.  
_Reducer이라는 이름은 Array.reduce에서 따온거다_  

## Reducer
리듀서는 다음의 규칙을 따라야한다.  
* 오직 `state`와 `action` 인자를 기반으로한 `new state` 계산만을 허용한다.
* 기존의 `state`에 직접 접근할 수 없다. 위에 설명한 불변성을 지켜야한다.
* 비동기 작동이나, 랜덤 함수 사용을 하면 안된다. 이 경우 "side effects"를 발생시킨다.
* 값을 변경하지 않더라도 기존의 state를 반환해야한다.  
다음은 Reducer이 따라야하는 규칙의 간단한 예시이다.

```js
const initialState = { value: 0 }

function counterReducer(state = initialState, action) {
  // Check to see if the reducer cares about this action
  if (action.type === 'counter/increment') {
    // If so, make a copy of `state`
    return {
      ...state,
      // and update the copy with the new value
      value: state.value + 1
    }
  }
  // otherwise return the existing state unchanged
  return state
}
```  

## 용어설명 2
* Store: Redux state는 **store**이라는 object안에서 존재한다. reducer을 통과함으로써 생성된다. getState라는 현재 value를 반환하는 함수도 
존재한다.  
```js
import { configureStore } from '@reduxjs/toolkit'

const store = configureStore({ reducer: counterReducer })

console.log(store.getState())
// {value: 0}
```

* Dispatch: **state를 변경할 수 있는 유일한 method이다. store.dispatch()로 action object를 통과시키면 된다.** 
```js
store.dispatch({ type: 'counter/increment' })

console.log(store.getState())
// {value: 1}
```  
dispatching 하는 것을 "triggering event"로 이해하면 좋다. 어떤 일이 발생했고, 그 일을 상태 저장하고 싶은 것이다. Reducer은 이때 
이벤트 리스너로 작동하는 것이다. dispatch는 보통 action creators를 사용해 다음과 같이 처리한다.  
```js
const increment = () => {
  return {
    type: 'counter/increment'
  }
}

store.dispatch(increment())

console.log(store.getState())
// {value: 2}
```  
* Selectors: 같은 데이터를 다양한 종류로 가공해서 추출하고 싶을 때 사용한다. 대형 프로젝트에서 불필요하게 반복되는 로직들을 줄여줄 수 있다.
```js
const selectCounterValue = state => state.value

const currentValue = selectCounterValue(store.getState())
console.log(currentValue)
// 2
```  
이런식으로 사용한다. 따로 메소드가 있는게 아니고.  
## Redux Data Flow
상술했던 "one-way data flow"와는 다르게, Redux data flow는 다른 특징들을 가지고 있다.  
* 초기 구성: root reducer function을 생성한다. store은 이것을 호출하고, initial state로 초기화한다.
* UI가 처음 렌더링되면, UI 컴포넌트는 각 state에 구독된다. useState와 비슷한듯.
![image](https://redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif)  

## 실제 사용
```js
import { createSlice } from '@reduxjs/toolkit';

export const slice = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
  },
  reducers: {
    increment: state => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1;
    },
    decrement: state => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = slice.actions;

// The function below is called a thunk and allows us to perform async logic. It
// can be dispatched like a regular action: `dispatch(incrementAsync(10))`. This
// will call the thunk with the `dispatch` function as the first argument. Async
// code can then be executed and other actions can be dispatched
export const incrementAsync = amount => dispatch => {
  setTimeout(() => {
    dispatch(incrementByAmount(amount));
  }, 1000);
};

// The function below is called a selector and allows us to select a value from
// the state. Selectors can also be defined inline where they're used instead of
// in the slice file. For example: `useSelector((state) => state.counter.value)`
export const selectCount = state => state.counter.value;

export default slice.reducer;
```  
* `setTimeout()`함수는 해당 초 이후에 내부 함수를 실행한다. 비동기로.
* `setInterval()`함수는 일정시간마다 반복되는 함수이다.
* 메모리 누수 조심: 페이지가 전환되지 않는 경우... 특히 싱글 페이지(SPA)인 경우 사용되지 않은 setTimeout() 코드가 메모리에 계속 남아 있을 수 있으며 가비지컬렉션(GB)에 의하여 회수 되지 않은 경우 성능저하의 원인이 된다. 반드시 setTimeout() 이벤트는 이벤트를 제거하는 코드 역시 필요하다. clearTimeout()은 설정된 setTimeout()을 제거하는 함수이다.  


## Redux Store 만들기
```js
import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';

export default configureStore({
  reducer: {
    counter: counterReducer,
  },
});
```  
초기 state를 counterReducer을 받아서 한다. couter: counterReducer로 초기 선언을 해줬다는 뜻은, state.counter의 영역을 
사용하겠다는 말이다. configureStore()는 여러가지 middleware을 자동으로 세팅해준다.
## Redux Slices
"Slice"란 Redux reducer logic의 묶음이다. 앱의 single feature마다 생성하면 된다.  
action creators들을 우리가 손으로 매번 작성할 수도 있지만, 너무 비효율적이다. `createSlice`라는 것을 사용하면 된다.  
```js
console.log(counterSlice.actions.increment())
// {type: "counter/increment"}
```
이런 식이다.  
Redux에서 불변성을 지켜야하는 이유는 여러가지가 있는데, 읽어보니까 그냥 간결성 일관성등등의 이유이다. 근데 계속 강조하는거 보니까 진짜 중요한듯.  
* It causes bugs, such as the UI not updating properly to show the latest values
* It makes it harder to understand why and how the state has been updated
* It makes it harder to write tests
* It breaks the ability to use "time-travel debugging" correctly
* It goes against the intended spirit and usage patterns for Redux  
```js
// ✅ This is safe, because we made a copy
return {
  ...state,
  value: 123
}
```  
이런식으로 해결하면 된다.  

## useSelector
```js
import React from 'react'
import { useSelector } from 'react-redux'

export const SinglePostPage = ({ match }) => {
  const { postId } = match.params

  const post = useSelector(state =>
    state.posts.find(post => post.id === postId)
  )

```
이런식으로 사용하면 된다. 주의사항은, useSelector에서 반환된 값은 state가 변화될 때마다 리렌더링 되는 것이다.  
* find에서 찾지 못하면 undefined를 반환한다.
* reducer에서 랜덤값과 같은 값을 계산하게 하면 안된다. uuid같은게 필요하면 그 전에 집어넣어라. 함수 같은걸 안에서 실행하고 싶으면 
```js
const postsSlice = createSlice({
  name: 'posts',
  initialState,
  reducers: {
    postAdded: {
      reducer(state, action) {
        state.push(action.payload)
      },
      prepare(title, content) {
        return {
          payload: {
            id: nanoid(),
            title,
            content
          }
        }
      }
    }
    // other reducers here
  }
})
```  
처럼 쓰면 된다. prepare callback 메소드를 제공해주는 것이다.  
  
## 포스트 리액션 버튼
https://redux.js.org/tutorials/essentials/part-4-using-data#post-reaction-buttons


# Async Logic
지금까지 한건 로컬에서 작동하는거고, 보통은 API 호출이 필요하다. redux-thunk라는 middleware을 사용한다 보통. 플로우는 다음과 같다.
![image](https://redux.js.org/assets/images/ReduxAsyncDataFlowDiagram-d97ff38a0f4da0f327163170ccc13e80.gif)  

* API 서버로 글을 작성할 때에는, 클라이언트에서 랜덤값을 생성하는 행위를 하지 않아도 된다. 즉, 서버에서 그것을 처리하기 때문에 request body를 title, content, userId만 보내도 된다. 그러면 서버에서 다른 extra informations를 포함한 값을 반환할 것이다.  
```js
export const addNewPost = createAsyncThunk(
  'posts/addNewPost',
  // The payload creator receives the partial `{title, content, user}` object
  async initialPost => {
    // We send the initial data to the fake API server
    const response = await client.post('/fakeApi/posts', { post: initialPost })
    // The response includes the complete post object, including unique ID
    return response.post
  }
)
```  
https://redux.js.org/tutorials/essentials/part-5-async-logic#sending-data-with-thunks
  
# Performance and Normalizing Data


