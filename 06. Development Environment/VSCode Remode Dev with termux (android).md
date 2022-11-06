# VSCode Remode Dev with termux (android)
1. Install `Termux` on https://f-droid.org/en/packages/com.termux/ (play store version is deprecated)
2. Run commands on pure termux
```
$pkg install openssh
$sshd
```
3. Change your password with `passwd`.
4. Find your ip via `ifconfig`.
5. Default termux ssh port is `8022`.
6. Connect ssh. ex) `ssh 10.10.10.1 -p 8022`
7. Install Ubuntu on your termux instance. (CLI Only) https://github.com/tuanpham-dev/termux-ubuntu
```bash
pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/tuanpham-dev/termux-ubuntu/master/ubuntu.sh && chmod +x ubuntu.sh && bash ubuntu.sh nde
```
7. Start ubuntu. `./start-ubuntu20.sh`
8. `sudo apt update && sudo apt install openssh-server`
9. `apt-get install build-essential -y` (for vscode remote requirements)
10. `nano /etc/ssh/sshd_config` and change line `PermitRootLogin yes` and `PasswordAuthentication yes`
11. `mkdir -p /run/sshd`
12. `/sbin/sshd -p 8023`
13. Test with `ssh USER_NAME_HERE@localhost -p 8023`


> @Poxios, 2022