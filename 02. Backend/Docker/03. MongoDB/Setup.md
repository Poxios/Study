### Install Image
```cmd
docker pull mongo
```

### Run Image
* Use `${PWD}` on Powershell.
```cmd
docker run --name mongodb-container -v ~/data:/data/db -d -p 27017:27017 mongo
docker run --name mongodb-container -v ${PWD}/data:/data/db -d -p 27017:27017 mongo
```

### Connect to Image
```cmd
docker exec -it mongodb-container bash
```

### ETC
* Make `.ps1` file in your MongoDB folder to open it fast.