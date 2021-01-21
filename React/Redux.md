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
