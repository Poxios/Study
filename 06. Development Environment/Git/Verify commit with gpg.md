## Full Settings
* https://velog.io/@bigsaigon333/github-verified-commit-%ED%95%98%EA%B8%B0

## Export and Import GPG Keys
* https://makandracards.com/makandra-orga/37763-gpg-extract-private-key-and-import-on-different-machine
1. List private key and remember your RSA unique id.
```bash
gpg --list-secret-keys user@example.com
```
2. Export it.
```bash
gpg --export-secret-keys YOUR_ID_HERE > private.key
```
3. Import it.
```bash
gpg --import private.key
```
4. After import gpg key, connect your GPG key to git.
```bash
git config --global user.signingkey 35F5FFB2
```