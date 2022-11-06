# How to run jsmpeg-vnc with https
1. Get `jsmpeg-vnc` from https://github.com/phoboslab/jsmpeg-vnc
2. Open `jsmpeg-vnc` folder and search for `ws://` -> change it to `wss://`. (for using secured web socket)
3. Run `nginx-reverse-proxy` with docker and set proxy pass to `http://host.docker.internal:8811`
4. Run `jsmpeg-vnc`
```cmd
jsmpeg-vnc.exe -f 60 -p 8811 "desktop"
```

> by @Poxios, 2022