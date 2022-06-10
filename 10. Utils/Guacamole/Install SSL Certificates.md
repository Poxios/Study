# Install SSL Certificates
## Install CertBot on WSL
[Link](https://hoing.io/archives/4491)
```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot
sudo apt-get install python3-certbot-nginx
sudo certbot --nginx -d www.MYDOMAIN.COM --email MY@EMAIL.com --agree-tos
```

## Remove Firewall on WSL
[Link](https://webisfree.com/2021-07-14/wsl2-%EC%99%B8%EB%B6%80-remote-ip-%EC%A0%91%EC%86%8D-%EA%B0%80%EB%8A%A5%ED%95%98%EB%8F%84%EB%A1%9D-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0-%EB%B0%A9%ED%99%94%EB%B2%BD-%ED%95%B4%EC%A0%9C)  
`PS> Set-ExecutionPolicy RemoteSigned`  

```powershell
$remoteport = bash.exe -c "ifconfig eth0 | grep 'inet '"
$found = $remoteport -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';

if( $found ){
  $remoteport = $matches[0];
} else{
  echo "The Script Exited, the ip address of WSL 2 cannot be found";
  exit;
}

#[Ports]
#All the ports you want to forward separated by coma
$ports=@(80, 1000,2000,3000,5000);


#[Static ip]
#You can change the addr to your ip config to listen to a specific address
$addr='0.0.0.0';
$ports_a = $ports -join ",";


#Remove Firewall Exception Rules
iex "Remove-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' ";

#adding Exception Rules for inbound and outbound Rules
iex "New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Outbound -LocalPort $ports_a -Action Allow -Protocol TCP";
iex "New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Inbound -LocalPort $ports_a -Action Allow -Protocol TCP";

for( $i = 0; $i -lt $ports.length; $i++ ){
  $port = $ports[$i];
  iex "netsh interface portproxy delete v4tov4 listenport=$port listenaddress=$addr";
  iex "netsh interface portproxy add v4tov4 listenport=$port listenaddress=$addr connectport=$port connectaddress=$remoteport";
}
```  
Execute this script (.ps1)


### ifconfig error
`sudo apt-get install net-tools` in WSL.

### Check firewall
Show: `netsh interface portproxy show v4tov4`  
Reset: `netsh interface portproxy reset`  

## ETC
* Add your ip in `DNS TABLE - A`.
* You need add `www.` domain in your `DNS TABLE - A`.

## Offical Docs
* https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/

# Apply with ZeroSSL
* https://app.zerossl.com/images/zerossl_logo.svg
## Fix Certificates Error
`cat certificate.crt ca_bundle.crt > bundle_chained.crt`  
Merge them with correct order!!!  
Bundle file is last!!!
  
And place .crt, .key files to ngrok/ssl folder and restart docker-compose  
`docker-compose restart` 