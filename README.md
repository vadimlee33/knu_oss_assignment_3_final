# Assignment 3

First of all, you have to install Docker on your PC.

#### Download and Install here:
```
https://www.docker.com/products/docker-desktop/
```
Then download Dockerfile and build image.
#### Building image:
```
docker build -t ANY_TAG .
```

#### Running container:
```
docker run -d -p 8080:8080 ANY_TAG:latest
```

#### Check the program:
```
curl -X POST 'http://localhost:8080/numbers?new=123'

curl -X GET 'http://localhost:8080/numbers/average'
curl -X GET 'http://localhost:8080/numbers/sum'
curl -X GET 'http://localhost:8080/numbers/stddev'
```
WARNING: run the commands in single quotes or you will get an error
