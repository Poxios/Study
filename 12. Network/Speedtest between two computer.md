# Speedtest between two computer
* https://tuxtweaks.com/2014/11/linux-network-speed-test/
## Start netcat to listen
```
nc -lk 2112 > /dev/null
```

## Send data 
```
dd if=/dev/zero bs=90000 count=625 | nc -v TARGET_PC_IP_HERE TARGET_PORT_HERE
```