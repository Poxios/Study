# Use full disk space after install Ubuntu
* https://seungjuitmemo.tistory.com/352
1. Check disk spaces
```
df -hT
```

2. Check max disk space
```
vgdisplay
```

3. Check current usage
```
lvscan
```

4. Maximize volume
```
lvextend -l +100%FREE -n /dev/ubuntu-vg/ubuntu-lv
```

5. Check volume expanded successfully
```
lsblk
```

6. Resize filesystem
```
resize2fs /dev/ubuntu-vg/ubuntu-lv
```