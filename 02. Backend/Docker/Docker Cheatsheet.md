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

### 