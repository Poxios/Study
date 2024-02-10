https://stackoverflow.com/questions/1098040/checking-if-a-key-exists-in-a-javascript-object
  
`obj['key']===undefined` 이러면 실제 값이 undefined일때 곤란해진다.  
"key" in obj 이래도 된다  
obj.hasOwnProperty("key") 이래도 된다  
  
속도는 ===으로 체크하는게 제일 빠르고, 다음으로 hasOwnProperty, 마지막으로 in이 가장 느리다.
