
```yml
version: "3"
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: nginx-proxy-manager
    restart: unless-stopped
    networks:
      - "npm_network"
      - "npm_internal"
    ports:
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
    environment:
      DB_MYSQL_HOST: "npm_db"
      DB_MYSQL_PORT: 3306
      DB_MYSQL_USER: "npm"
      DB_MYSQL_PASSWORD: "PASSWORD_HERE"
      DB_MYSQL_NAME: "npm"
    # To connect outside of docker.
    extra_hosts:
      - "host.docker.internal:host-gateway"
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    depends_on:
      - npm_db

  npm_db:
    image: 'jc21/mariadb-aria:latest'
    container_name: nginx-proxy-manager-db
    restart: unless-stopped
    networks:
      - "npm_internal"
    environment:
      MYSQL_ROOT_PASSWORD: 'PASSWORD_HERE'
      MYSQL_DATABASE: 'npm'
      MYSQL_USER: 'npm'
      MYSQL_PASSWORD: 'PASSWORD_HERE'
    volumes:
      - ./data/mysql:/var/lib/mysql

  
networks:
  npm_network:
    name: npm_network
  npm_internal:
    external: false
```