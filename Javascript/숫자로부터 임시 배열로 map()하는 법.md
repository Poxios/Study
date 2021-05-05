## Using spread operator (...) and keys method
```js
[ ...Array(N).keys() ].map( i => i+1);
```

## Fill/Map
```js
Array(N).fill().map((_, i) => i+1);
```

## Array.from
```js
Array.from(Array(N), (_, i) => i+1)
```

## Array.from and { length: N } hack
```js
Array.from({ length: N }, (_, i) => i+1)
```

## Note about generalised form
All the forms above can produce arrays initialised to pretty much any desired values by changing i+1 to expression required (e.g. i*2, -i, 1+i*2, i%2 and etc). If expression can be expressed by some function f then the first form becomes simply
```js
[ ...Array(N).keys() ].map(f)
```
