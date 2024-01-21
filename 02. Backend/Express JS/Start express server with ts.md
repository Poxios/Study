# Start express server with ts
1. init
```
yarn
yarn add express
yarn add -D typescript @types/node @types/express
npx tsc --init
```
  
2. Add code below
```
"scripts": {
    "start": "tsc && node dist/server/index.ts"
  }
```
* https://kis6473.tistory.com/108
