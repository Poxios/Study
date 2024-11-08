# Make gpg key and register to github (MacOS)
1. Install `gpg`
```
brew install gnupg
```
  
2. Generate key (do not enter the passphrase)
```
gpg --full-generate-key
```
  
3. Go to [Github](https://github.com) -> Setting -> GPG keys (left side bar) -> New GPG Key -> Paste your gpg keys (commands below)
```
gpg --list-secret-keys --keyid-format LONG
gpg --armor --export B7D77A4BA5D85444
```

4. Register key to local git
```
git config --global user.signingkey YOUR_LONG_KEY
git config --global commit.gpgSign true
```

  
### Troubleshooting
* `gpg: signing failed: Inappropriate ioctl for device` -> just run this command and add to `.zshrc`
```
export GPG_TTY=$(tty)
```

### Export key to use other computer
```
gpg --export-secret-keys --armor B7D77A4BA5D85444 > mykey.asc
```

### Import (is it working?)
```
gpg --import mykey.asc
git config --global user.signingkey "mykey"
```
