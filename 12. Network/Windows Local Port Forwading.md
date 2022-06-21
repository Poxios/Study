## Make Forwarding
```powershell
netsh interface portproxy add v4tov4 listenaddress=127.0.0.1 listenport=9000 connectaddress=192.168.0.10 connectport=80
```
## List it
```powershell
netsh interface portproxy show v4tov4
```

## Remove it
```powershell
netsh interface portproxy delete v4tov4 listenport=3389 listenaddress=127.0.0.1
```