# Send file p2p fastest
### Receiver
```
nc -l PORT_NUMBER > RECEIVED_FILE_NAME
```

### Sender
```
cat FILE_NAME > nc -q 1 -v TARGET_PC_IP TARGET_PC_PORT
```
or (if `-q` argument not working)
```
cat FILE_NAME > nc -v TARGET_PC_IP TARGET_PC_PORT
```
* remove `-v` argument if not working

---
## More
* https://unix.stackexchange.com/questions/48399/fast-way-to-copy-a-large-file-on-a-lan
```
# Receiver Side (Destination)
nc -q 1 -l -p PORT_HERE | tar xv
or (mac)
nc -l 2112 | pv -pterb -s 100g > RECEIVED_FILE_NAME
or (without progress bar)
nc -l 2112 > RECEIVED_FILE_NAME

# Sender Side (Source)
tar cv . | nc -q 1 dest-ip 1234
```

## Better way with progress bar (receiver side)
```
nc -l 2112 | pv -pterb -s 100g > RECEIVED_FILE_NAME
or (no file size)
nc -l 2112 | pv -terb > RECEIVED_FILE_NAME
```
