# Send file p2p fastest
* https://unix.stackexchange.com/questions/48399/fast-way-to-copy-a-large-file-on-a-lan
```
user@dest:/target$ nc -q 1 -l -p PORT_HERE | tar xv

user@source:/source$ tar cv . | nc -q 1 dest-ip 1234
```

## Better way with progress bar
```
nc -l 2112 | pv -pterb -s 100g > RECEIVED_FILE_NAME
or (no file size)
nc -l 2112 | pv -terb > RECEIVED_FILE_NAME
```