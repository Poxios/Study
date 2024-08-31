## Send large size file (archive, encrypt, split)
1. Use python http server and download with wget
### Sender
```
python -m http.server 7711 .
```

### Receiver
```
wget DESTNIATION_URL
```

2. Use tar, 
```
tar cvf DESTINATION_FILE_PATH
gpg -c DESTINATION_FILE_PATH
split -b 300M FILE_NAME FILE_NAME
```
