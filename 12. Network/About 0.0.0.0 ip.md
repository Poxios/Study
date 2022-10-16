```js
// ! [Server] Start Listening
app.listen({ port: 3000, host: '0.0.0.0' }, (err, address) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`[DEV] Server Started at ${address}`);
});
```

* Want to reveal server's ip to any address