```yaml
# Simple docker-compose file example for Traefik 
# Feature: Let's encrypt(ACME), Log(Debug level), Secure Dashboard(https connection, require password), Redirect http requests to https, Example docker container connection(whoami)
# @Poxios, 2022

version: '3'

services:
  reverse-proxy:
    image: traefik
    container_name: reverse-proxy
    command:
      - "--log.level=DEBUG"
      - "--api.dashboard=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.websecure.address=:443"
      - "--entrypoints.web.address=:80"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=YOUR@EMAIL.COM"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
    networks:
      - "traefik_network"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./letsencrypt:/letsencrypt
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.traefik_https.rule=Host(`YOUR.DOMAIN.HERE`)"
      - "traefik.http.routers.traefik_https.entrypoints=websecure"
      - "traefik.http.routers.traefik_https.tls=true"
      - "traefik.http.routers.traefik_https.tls.certResolver=myresolver"
      - "traefik.http.routers.traefik_https.service=api@internal"
      - "traefik.http.routers.traefik_https.middlewares=traefik-auth"
      - "traefik.http.middlewares.traefik-auth.basicauth.users=adminuser:YOUR_PASSWORD_FROM_HTPASSWD"

      - "traefik.http.routers.traefik.entrypoints=web"
      - "traefik.http.routers.traefik.rule=Host(`YOUR.DOMAIN.HERE`)"
      - "traefik.http.routers.traefik.middlewares=traefik-https-redirect"
      - "traefik.http.middlewares.traefik-https-redirect.redirectscheme.scheme=https"
    
  whoami:
    image: "traefik/whoami"
    container_name: "simple-service"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.whoami.rule=Host(`YOUR.DOMAIN.HERE`) && Path(`/traefik`)"
      - "traefik.http.routers.whoami.entrypoints=websecure"
      - "traefik.http.routers.whoami.tls.certresolver=myresolver"
    networks:
      - "traefik_network"

networks:
  traefik_network:
    name: traefik_network
```

