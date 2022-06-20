### Install Image
```cmd

```

### Run Image
* Use `${PWD}` on Powershell.
```cmd
docker run --name mongodb-container -v ~/data:/data/db -d -p 27017:27017 mongo
docker run --name mongodb-container -v ${PWD}:/data/db -d -p 27017:27017 mongo
```

### Connect to Image
```cmd
docker exec -it mongodb-container bash
```