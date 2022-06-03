# Use https on dev
1. install mkcert
2. `mkcert -key-file key.pem -cert-file cert.pem example.com *.example.com localhost 127.0.0.1`
3. `mkcert -install` to install cert files on local computer (dev only)
4. move `key.pem`, `cert.pem` files to express workspace, and load these files.