## 환경
* js / ts 동시에 사용하는 상황이다.
## 해결
```json
...
// package.json
 "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ],
    "rules": {
      "no-unused-vars": 0,
      "@typescript-eslint/no-unused-vars": "off"
    }
  },
...
```
