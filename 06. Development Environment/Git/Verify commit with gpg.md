## Full Settings
* https://velog.io/@bigsaigon333/github-verified-commit-%ED%95%98%EA%B8%B0

## Export and Import GPG Keys
* https://makandracards.com/makandra-orga/37763-gpg-extract-private-key-and-import-on-different-machine
1. Turn on GPG key signing global.
```bash
git config --global commit.gpgsign true
```
2. List private key and remember your RSA unique id.
```bash
gpg --list-secret-keys user@example.com
```
3. Export it.
```bash
gpg --export-secret-keys YOUR_ID_HERE > private.key
```
4. Import it.
```bash
gpg --import private.key
```
5. After import gpg key, connect your GPG key to git.
```bash
git config --global user.signingkey 35F5FFB2
```