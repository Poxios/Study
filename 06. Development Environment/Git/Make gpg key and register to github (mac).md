# Make gpg key and register to github (MacOS)
1. Install `gpg`
```
brew install gnupg
```
  
2. Generate key
```
gpg --full-generate-key
```
  
3. Go to [Github](https://github.com) -> Setting -> GPG keys (left side bar) -> New GPG Key -> Paste your gpg keys (commands below)
```
gpg --list-secret-keys --keyid-format LONG
gpg --armor --export B7D77A4BA5D85444
```
  
### Troubleshooting
* `gpg: signing failed: Inappropriate ioctl for device` -> just run this command
```
export GPG_TTY=$(tty)
```
