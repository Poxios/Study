# Guacamole
## 언제 어디서나 Chromium만 있으면 원격제어 사용하기
`https://it-svr.com/apche-guacamole-docker/`  
* 위 링크에서 참고
  
## 사용하면 되는 유틸들
1. WSL2
2. Guacamole
3. Docker-Compose
4. Ngrok
  
## 하는 법
1. WSL2를 활성화 후 WSL2 버전의 Ubuntu를 설치한다 (Ubuntu를 WSL2로 변환작업 필요)
2. Docker 설정에 들어가서 WSL2 Container - Ubuntu를 활성화 한다.
3. `cd guacamole-docker-compose` 입력 후 `code .`로 `docker-compose` 파일을 수정한다.
4. `guacamole:` - `environment:` - 하단에 `TOTP_ENABLED: ‘true’`를 입력하면 Google OTP를 사용할 수 있다.
```yml
  guacamole:
    container_name: guacamole_compose
    depends_on:
    - guacd
    - postgres
    environment:
      GUACD_HOSTNAME: guacd
      POSTGRES_DATABASE: guacamole_db
      POSTGRES_HOSTNAME: postgres
      POSTGRES_PASSWORD: 'ChooseYourOwnPasswordHere1234'
      POSTGRES_USER: guacamole_user
      TOTP_ENABLED: 'true'
```
5. 스크롤을 더 내려서 `nginx` 파트에서 ports를 https인 443을 먹인다. 또한 Docker Container 내부에서 Host에 접속하기 위해서 extra_hosts에 다음을 추가한다.
```yml
# nginx
  nginx:
   container_name: nginx_guacamole_compose
   restart: always
   image: nginx
   volumes:
   - ./nginx/ssl/self.cert:/etc/nginx/ssl/self.cert:ro
   - ./nginx/ssl/self-ssl.key:/etc/nginx/ssl/self-ssl.key:ro
   - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
   - ./nginx/mysite.template:/etc/nginx/conf.d/default.conf:ro
   ports:
   - 443:443
   extra_hosts:
   - "host.docker.internal:host-gateway"
```
7. Ubuntu 실행 후 다음의 코드를 입력한다
```shell
git clone "https://github.com/boschkundendienst/guacamole-docker-compose.git"

./prepare.sh
docker-compose up -d
```
8. 모두 실행이 완료 되면 ngrok 윈도우 버전을 설치하고 `ngrok http 443` 를 입력한다.
9. 완료

## 원리
* 리눅스 기반의 Docker에서 실행되는 과카몰리를 WSL2에서 실행한다.
* Docker의 `host.docker.internal`를 사용하여 호스트 RDP에 접속한다.
* Ngrok으로 local 443포트를 오픈한다.

---
### 혹시 몰라서 docker-compose 다 올려놓음
```yml
version: '2.0'

# networks
# create a network 'guacnetwork_compose' in mode 'bridged'
networks:
  guacnetwork_compose:
    driver: bridge

# services
services:
  # guacd
  guacd:
    container_name: guacd_compose
    image: guacamole/guacd
    networks:
      guacnetwork_compose:
    restart: always
    volumes:
    - ./drive:/drive:rw
    - ./record:/record:rw
  # postgres
  postgres:
    container_name: postgres_guacamole_compose
    environment:
      PGDATA: /var/lib/postgresql/data/guacamole
      POSTGRES_DB: guacamole_db
      POSTGRES_PASSWORD: 'ChooseYourOwnPasswordHere1234'
      POSTGRES_USER: guacamole_user
    image: postgres:13.4
    networks:
      guacnetwork_compose:
    restart: always
    volumes:
    - ./init:/docker-entrypoint-initdb.d:ro
    - ./data:/var/lib/postgresql/data:rw

  # guacamole
  guacamole:
    container_name: guacamole_compose
    depends_on:
    - guacd
    - postgres
    environment:
      GUACD_HOSTNAME: guacd
      POSTGRES_DATABASE: guacamole_db
      POSTGRES_HOSTNAME: postgres
      POSTGRES_PASSWORD: 'ChooseYourOwnPasswordHere1234'
      POSTGRES_USER: guacamole_user
      TOTP_ENABLED: 'true'
    image: guacamole/guacamole
    links:
    - guacd
    networks:
      guacnetwork_compose:
    ports:
## enable next line if not using nginx
##    - 8080:8080/tcp # Guacamole is on :8080/guacamole, not /.
## enable next line when using nginx
    - 8080/tcp
    restart: always

########### optional ##############
  # nginx
  nginx:
   container_name: nginx_guacamole_compose
   restart: always
   image: nginx
   volumes:
   - ./nginx/ssl/self.cert:/etc/nginx/ssl/self.cert:ro
   - ./nginx/ssl/self-ssl.key:/etc/nginx/ssl/self-ssl.key:ro
   - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
   - ./nginx/mysite.template:/etc/nginx/conf.d/default.conf:ro
   ports:
   - 443:443
   extra_hosts:
   - "host.docker.internal:host-gateway"
   links:
   - guacamole
   networks:
     guacnetwork_compose:
   # run nginx
   command: /bin/bash -c "nginx -g 'daemon off;'"
# nginx-debug-mode
#   command: /bin/bash -c "nginx-debug -g 'daemon off;'"
####################################################################################

```