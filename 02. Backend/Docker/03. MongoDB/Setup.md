### Install Image
```cmd

```

### Run Image
```cmd
docker run --name mongodb-container -v ~/data:/data/db -d -p 27017:27017 mongo
```

### Connect to Image
```cmd
docker exec -it mongodb-container bash
```