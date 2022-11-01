## Jenkins Setup
### Install on Windows
![Err](https://www.jenkins.io/doc/book/resources/tutorials/windows-invalid-service-logon-credentials.png)
https://www.jenkins.io/doc/book/installing/windows/#invalid-service-logon-credentials

### Install on Linux Docker
```
sudo docker run -d --name jenkins -p 8080:8080 -e JENKINS_OPTS=--prefix=/jenkins -v /jenkins:/var/jenkins_home -v /usr/bin/docker:/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -u root jenkins/jenkins:lts 
```
* `prefix` - Nginx 리버스 프록시를 위해 사용
* `docker volume` - 호스트의 도커를 사용하기 위해 사용