### Download Image
```cmd
docker pull mariadb
```

### Start Image
* With volume settings
```cmd
docker run --name mariadb -d -p 3306:3306 --restart=always -e MYSQL_ROOT_PASSWORD=root mariadb
```
* With volume settings
```cmd
docker container run -d -p 13306:3306 -e MYSQL_ROOT_PASSWORD=pwd123 -v ${PWD}/data:/var/lib/mysql --name mariadb_local mariadb
```

### Connect to DB
```cmd
docker exec -it mariadb /bin/bash
```

