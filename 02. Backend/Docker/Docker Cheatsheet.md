`Made by @Poxios 2022`  
## Docker Cheatsheet
### Build Image File
**Command**  
`docker build -t IMAGE_FILE_NAME_HERE DOCKER_FILE_LOCATION_HERE`  
**Example**  
`docker build -t getting-started .`  

### Run
**Command**  
`docker run -dp 3000:3000 IMAGE_NAME_HERE`  
`-d` detached mode == background mode  
`-p` port mapping  
**Example**  
`docker run -dp 3000:3000 getting-started`  

### Remove a container
`docker ps`
`docker stop CONTAINER_ID`
`docker rm CONTAINER_ID`
  
**Do it at once**  
`docker rm -f CONTAINER_ID`
  
**Or**
Remove it using the Docker Dashboard
### Login to Docker Hub
`docker login -u DOCKER_ID`  

### List Docker Image
`docker image -i`  

### Change Image Tag Name
`docker tag getting-started YOUR-USER-NAME/getting-started`  

### Persist Data - with volume control
`docker volume create todo-db`  
`docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started`  
**Inspect Volume**
`docker volume inspect todo-db`  

### Mount host dir
```powershell
docker run -dp 3000:3000 `
     -w /app -v "$(pwd):/app" `
     node:12-alpine `
     sh -c "yarn install && yarn run dev"
```
`$(pwd)`: current dir  

### Make New Network
`docker network create todo-app`  

### Run MySQL with environment variables
```powershell
docker run -d `
     --network todo-app --network-alias mysql `
     -v todo-mysql-data:/var/lib/mysql `
     -e MYSQL_ROOT_PASSWORD=secret `
     -e MYSQL_DATABASE=todos `
     mysql:5.7
```

### Network Troubleshooting
`docker run -it --network todo-app nicolaka/netshoot`  
`dig mysql` (hostname required)  

### Execute Command to running container
`docker exec -it elegant_driscoll mysql -u root -p`  

### Kill All Containers
`docker kill $(docker ps -q)`  

### 