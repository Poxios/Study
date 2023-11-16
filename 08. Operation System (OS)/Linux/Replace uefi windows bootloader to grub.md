# Replace uefi windows bootloader to grub
* https://thingsandcode.com/linux/how-to-replace-windows-bootloader-with-grub2/
### Backup
```
dd if=/dev/sda2 of=./efi_backup.image
```

### Process
```
os-prober
dd if=/dev/sda2 of=./efi_backup.image
sudo grub-install --target=x86_64-efi --efi-directory=/mnt/efi /dev/yyyyy
sudo grub-mkconfig -o /boot/efi/EFI/ubuntu/grub.cfg
```

### 
```
https://rafat-joy99.medium.com/pc-boots-straight-into-windows-10-instead-of-launching-grub-76b01fe89d67
# Windows Side
bcdedit /set "{bootmgr}" path \EFI\ubuntu\grubx64.efi
# Ubuntu Side
sudo update-grub
```