### Download Image
```cmd
docker pull mariadb
```

### Start Image
```cmd
docker run --name mariadb -d -p 3306:3306 --restart=always -e MYSQL_ROOT_PASSWORD=root mariadb
```
* With volume settings
```cmd
docker container run -d -p 13306:3306 -e MYSQL_ROOT_PASSWORD=pwd123 -v ${PWD}/data:/var/lib/mysql --name mariadb_local mariadb
docker container run -d -p 13306:3306 -e MYSQL_ROOT_PASSWORD=pwd123 -v ${PWD}/data:/var/lib/mysql --name mysql_local mysql
```
* With user name, password
```
docker run --name my_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root_password -e MYSQL_DATABASE=dalcom -e MYSQL_USER=dalcom_admin -e MYSQL_PASSWORD=thisispassword123! -v ${PWD}/data:/var/lib/mysql -d mysql:8
```

### Connect to DB
```cmd
docker exec -it mariadb /bin/bash
```
