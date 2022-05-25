```json
"start-production": "set NODE_ENV=production&& node --max-old-space-size=4096 -- node_modules/ts-node/dist/bin --transpile-only -P tsconfig.json src/index.ts",
    "start": "nodemon --exec node --max-old-space-size=4096 -- node_modules/ts-node/dist/bin --transpile-only -P tsconfig.json src/index.ts",
```