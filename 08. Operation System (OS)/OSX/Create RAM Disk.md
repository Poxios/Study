# Create RAM Disk
## Attach
```
diskutil erasevolume APFS 'RAM Disk' `hdiutil attach -nobrowse -nomount ram://1048576`
```

## Detach
```
hdiutil detach /dev/disk2
```
## force
```
sudo hdiutil detach /dev/disk2 -force
```
