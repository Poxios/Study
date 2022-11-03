```bash
sudo chmod -R 600 ./letsencrypt/acme.json
```

```yaml
version: '3'

services:
  reverse-proxy:
    image: traefik
    container_name: reverse-proxy
    command:
      - "--log.level=DEBUG" # For debugging acme generation
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=EMAIL_HERE"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
```

