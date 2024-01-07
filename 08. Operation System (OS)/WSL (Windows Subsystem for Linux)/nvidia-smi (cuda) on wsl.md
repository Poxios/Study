# nvidia-smi (cuda) on wsl.md
1. Add nvidia cuda gpg key 
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
```

2. List available driver versions
```
apt-cache search nvidia-utils-
```

3. Install latest nvidia-utils
```
sudo apt install nvidia-utils-535
```
