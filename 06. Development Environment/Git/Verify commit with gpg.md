## Full Settings
* https://velog.io/@bigsaigon333/github-verified-commit-%ED%95%98%EA%B8%B0

## Export and Import GPG Keys (GPG key migration) (A PC to B PC)
* https://makandracards.com/makandra-orga/37763-gpg-extract-private-key-and-import-on-different-machine
> Default path for `gpg.exe` on windows is `C:\Program Files\Git\usr\bin\gpg.exe`.
1. (PC A) List private key and remember your RSA unique id.
```bash
gpg --list-secret-keys user@example.com
```
1. (PC A) Export it.
```bash
gpg --export-secret-keys YOUR_ID_HERE(something long above) > private.key
```
1. (PC B) Import it.
```bash
gpg --import private.key
```
1. (PC B) After import gpg key, register your GPG key to git and enable GPG signing globally.
```bash
git config --global commit.gpgsign true
git config --global user.signingkey 35F5FFB2
```

## Remember GPG password when signing git commits
You can set a timeout period for gpg-agent in ~/.gnupg/gpg-agent.conf with this line:  
```
default-cache-ttl 3600
```