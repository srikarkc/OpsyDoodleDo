# Class 6 - Dec' 9, '23 - Docker

## Introduction
![Docker Logo](https://www.docker.com/wp-content/uploads/2023/08/logo-dont-spacing.svg)

> Docker is a platform for running applications in lightweight containers.

---

# Introduction

Why is Docker important?

Containers share the Linux Kernel and thus are lightweight compared to VMs.

An Ubuntu VM without GUI is around 1GB in size whereas Alpine Linux is around 5MB.

VMs take minutes to come up while containers can be brought up in seconds.

Language interpreters and software library dependecy issues between different environments can be resolved using Docker.


Which Linux technologies enable containers?
CGroups and Namespaces


Docker works only on Linux Kernel. On Windows and MacOS, it runs on a Linux VM.
Docker is NOT a programming language and NOT a framework.

Container is a running instance of an image. 
Image is a bundled snapshot of all the files that should be available to a program running in a container.


### Installed Docker

Used the convenience script available at docker.io/download then Docker Engine - Linux - Ubuntu

Added user to Docker group

`docker run hello-world`

The hello-world image was not found in the local so it was pulled from Registry (Docker Hub).

`docker ps` - See all running containers

`docker images` - See all images

Container ID - random characters - uniquely different for each container

Image ID - SHA256 - Deterministic (it will be the same for all of us)

`docker stop <image_id>` - Stop a running Container

`docker start <image_id>` - Start a container that was stopped

--detach option - Let's us run containers in the background

--interactive - Keeps the STDIN stream open for the container even if no terminal is attached

--tty - These attach the container's terminal to our current terminal

Manually detach container - Ctrl + P Q (keep holding ctrl)

--link - Legacy command to link container networks

--name - Name of the Container


### Docker logs

`docker logs <container_name>`

Docker captures STDOUT & STDERR of the container's main process (PID 1)

They are stored in JSON at \/var/lib/docker/containers/<container_id>/<container_logs.json>

These logs are stored in the host system's storage


### Isolation

We saw that PID 1 of 2 different containers are running different processes. This is possible through Linux namespaces technology.

![Docker Lifecycle](https://miro.medium.com/v2/resize:fit:1083/1*G_zpPbsTusaoaBONuD43ow.png)

`docker exec -it <container_id> /bin/sh`



Filesystem isolation:

Linux has a directory tree.

![Directory tree](https://www.devopsschool.com/blog/wp-content/uploads/2023/06/Linux-file-systems-827x1024.jpeg)

Each container has it's own isolated FS.

`docker run -d --name wp --read-only wordpress:5.0.0-php7.2-apache`

The above command failed since apache writes to the FS while booting up

`docker run -d --name wp_writable wordpress:5.0.0-php7.2-apache`

Ran the command without read-only and then it started

`docker container diff wp_writable`

Showed the directories that were written to

`docker run -d --name wp2 --read-only -v /run/apache2 --tmpfs /tmp wordpress:5.0.0-php7.2-apache`

We used -v and --tmpfs to overcome the read-only challenges.

`docker run --env MY_ENVIRONMENT_VAR="test" busybox:latest env`

Use -e to pass environment variables



### Tags and remote repos

Create a Docker Hub account

Tag your image as <account_name>/<repository_name>:<tag>

`docker tag hello-world:latest srikarkc/hello-world:v1.0`

Login to remote repo

`docker login`

Push to remote repository

`docker push srikarkc/hello-world:v1.0`

Pull from remote repo

`docker pull srikarkc/hello-world:v1.0`

Remove image 

` docker rmi <image_id|name:tag>`



###  Saving images to a file

`docker pull busybox:latest`

`docker save -o myfile.tar busybox:latest`

`docker load -i myfile.tar`



### Docker volumes

1. Bind mount

We created a nginx configuration file and a log file on our host system.

We mounted these with type=bind to the container.
```
CONF_SRC=~/example.conf; \
CONF_DST=/etc/nginx/conf.d/default.conf; \

LOG_SRC=~/example.log; \
LOG_DST=/var/log/nginx/custom.host.access.log; \

docker run -d --name diaweb \
  --mount type=bind,src=${CONF_SRC},dst=${CONF_DST} \
  --mount type=bind,src=${LOG_SRC},dst=${LOG_DST} \
  -p 80:80 \
  nginx:latest
```

2. tmpfs mount

This mounts to the memory (RAM) and is used for private key files, database passwords, API key files, or other sensitive configuration files.
```
docker run --rm \
    --mount type=tmpfs,dst=/tmp \
    --entrypoint mount \
    alpine:latest -v
```

3. Docker volumes

Docker volumes are named filesystem trees managed by Docker.

`docker volume create --driver local --label example=location vol-example`

`docker volume inspect vol-example`

`docker volume create --driver local --label example=cassandra cass-shared`

`docker run -d --volume cass-shared:/var/lib/cassandra/data --name cass1 cassandra:2.2`

`docker run -it --rm --link cass1:cass cassandra:2.2 cqlsh cass`

--rm flag remove the container after it has stopped.


### Docker networks

1. Bridge network

Similar to virtual box, you are creating a new network to be used among containers.

2. Host network

Similar to running an application on the host system without container.

`docker port <container_id>`


### Resource constraints

1. CPU limits

--cpus <# of cpus>

`docker run -itd --cpus 0.5 busybox:latest`

2. Memory limits

-m \<amount of memory>


[Resource Constraints](https://docs.docker.com/config/containers/resource_constraints/)


### Dockerfile

Write a Dockerfile -> Build an image from the Dockerfile

[Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

## Next meeting

1. Run a couple of applications (3 apps - python/java/node.js)
2. Deploy Jenkins on Docker and create build pipelines
3. Docker compose
4. Docker swarm
5. Introduction to Kubernetes

---

HW:

Study SUID, SGID, Sticky bit

https://www.redhat.com/sysadmin/suid-sgid-sticky-bit
