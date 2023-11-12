# Fix error while installing nvidia-smi
```
cd /var/cache/apt/archives/
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-340_340.107-0ubuntu0~gpu18.04.1_amd64.deb
```
or
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/*nvidia*.deb
```
and
```
sudo apt -f install
```
