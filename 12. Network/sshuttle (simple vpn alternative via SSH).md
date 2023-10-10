# sshuttle (simple vpn alternative via SSH)
* https://github.com/sshuttle/sshuttle
```
#It's not directly mentioned in the documentation on how to do this, so here you go. This command will tunnel everything including DNS:
sshuttle --dns -vr user@yourserver.com 0/0 --ssh-cmd 'ssh -i /your/key/path.pem'
```