* https://www.igorkromin.net/index.php/2017/04/26/base64-encode-or-decode-on-the-command-line-without-installing-extra-tools-on-linux-windows-or-macos/
##윈도우에서 Base64 인코딩 및 디코딩
###Encode
`certutil -encode data.txt tmp.b64 && findstr /v /c:- tmp.b64 > data.b64`
###Decode
`certutil -decode data.b64 data.txt`
