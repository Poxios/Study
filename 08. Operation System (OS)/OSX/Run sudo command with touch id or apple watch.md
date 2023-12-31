# Run sudo command with touch id or apple watch
0. Change root user password in preparation for the situation to be recovered.
```
sudo passwd root
```
1. Open sudo file with nano
```
sudo nano /etc/pam.d/sudo
```
2. Add the line below to the first
```
auth       sufficient     pam_tid.so
```
