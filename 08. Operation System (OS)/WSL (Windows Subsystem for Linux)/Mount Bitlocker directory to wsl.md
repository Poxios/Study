# Mount Bitlocker directory to wsl
* Run this command to mount. (if drive label is `W:`)
```
sudo mount -t drvfs -w uid=1000,gid=1000 W: /mnt/w
```
  
* You can access to `cd /mnt/w`