# Disk speedtest on CLI
### Write
```
time dd if=/dev/zero bs=1024k of=tstfile count=1024
```
### Read
```
dd if=tstfile bs=1024k of=/dev/null count=1024
```
