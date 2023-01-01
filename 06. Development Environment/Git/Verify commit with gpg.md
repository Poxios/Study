## Full Settings
* https://velog.io/@bigsaigon333/github-verified-commit-%ED%95%98%EA%B8%B0

## Export and Import GPG Keys
* https://makandracards.com/makandra-orga/37763-gpg-extract-private-key-and-import-on-different-machine
> Default path for `gpg.exe` on windows is `C:\Program Files\Git\usr\bin\gpg.exe`.
1. Turn on GPG key signing global.
```bash
git config --global commit.gpgsign true
```
1. List private key and remember your RSA unique id.
```bash
gpg --list-secret-keys user@example.com
```
1. Export it.
```bash
gpg --export-secret-keys YOUR_ID_HERE(something long above) > private.key
```
1. Import it.
```bash
gpg --import private.key
```
1. After import gpg key, connect your GPG key to git.
```bash
git config --global user.signingkey 35F5FFB2
```

## Remember GPG password when signing git commits
You can set a timeout period for gpg-agent in ~/.gnupg/gpg-agent.conf with this line:  
```
default-cache-ttl 3600
```