```yaml
version: '3'

services:
  portainer:
    container_name: portainer
    image: portainer/portainer-ce:latest
    ports:
      - "9000:9000" # not https, use http to communicate with traefik
    volumes:
      - ./portainer_test:/data
      - /var/run/docker.sock:/var/run/docker.sock

    networks:
      - "traefik_network"

    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints: [node.role == manager]

    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.portainerR.rule=Host(`YOUR.DOMAIN.HERE`) && PathPrefix(`/portainer`)"
      - "traefik.http.routers.portainerR.entrypoints=websecure"
      - "traefik.http.routers.portainerR.tls=true"
      - "traefik.http.routers.portainerR.tls.certresolver=myresolver"
      - "traefik.http.middlewares.portainer-stripprefix.stripprefix.prefixes=/portainer"
      - "traefik.http.routers.portainerR.middlewares=portainer-stripprefix@docker"
      # - "traefik.http.services.portainerLB.loadbalancer.server.scheme=https" # not https
      - "traefik.http.services.portainerLB.loadbalancer.server.port=9000"

networks:
  traefik_network:
    external:
      name: traefik_network
```