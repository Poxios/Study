### Download Image
```cmd
docker pull mariadb
```

### Start Image
```cmd
docker run --name mariadb -d -p 3306:3306 --restart=always -e MYSQL_ROOT_PASSWORD=root mariadb
```

### Connect to DB
```cmd
docker exec -it mariadb /bin/bash
```