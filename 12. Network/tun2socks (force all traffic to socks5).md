## tun2socks (force all traffic to socks5) - Bypass ISP's tethering detection
1. Run `tun2socks` first
```
sudo ./tun2socks-darwin-arm64 -device utun124 -proxy socks5://192.168.191.88:1080
```
  
2. Add subnet to `utun124` interface (at other window)
```
sudo ifconfig utun124 198.18.0.1 198.18.0.1 up
```
  
3. Add routing rules to force all traffic pass to `utun124` 
```
sudo route add -net 1.0.0.0/8 198.18.0.1
sudo route add -net 2.0.0.0/7 198.18.0.1
sudo route add -net 4.0.0.0/6 198.18.0.1
sudo route add -net 8.0.0.0/5 198.18.0.1
sudo route add -net 16.0.0.0/4 198.18.0.1
sudo route add -net 32.0.0.0/3 198.18.0.1
sudo route add -net 64.0.0.0/2 198.18.0.1
sudo route add -net 128.0.0.0/1 198.18.0.1
sudo route add -net 198.18.0.0/15 198.18.0.1
```
  
4. Block ipv6 in your OS setting
  
5. (optional) to use ipv6, run these codes
```
sudo ifconfig utun124 inet6 2001:db8:1234:5678::1/64
sudo route add -inet6 default 2001:db8:1234:5678::1%utun124
```
6. Enable ipv6 in your OS setting
7. Done!
