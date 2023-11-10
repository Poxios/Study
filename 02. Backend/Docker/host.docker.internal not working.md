# When `host.docker.internal` not working
1. Get in the container
```
docker exec -it CONTAINER_NAME /bin/bash
or
docker exec -it CONTAINER_NAME /bin/sh
```
2. See your host's ip
```
cat /etc/hosts
```
3. Use it! (ex. `172.17.0.1`)
