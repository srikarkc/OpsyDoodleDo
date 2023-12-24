# Class 7 - Dec' 23, '23 - Docker

## Introduction
![Docker Logo](https://www.docker.com/wp-content/uploads/2023/08/logo-dont-spacing.svg)

> Docker is a platform for running applications in lightweight containers.

---

### Union Filesystem

A Union Filesystem is a type of filesystem that layers multiple directories on top of each other into a single, unified view. This approach allows for a combination of read-only and read-write file systems, commonly used in operating systems and containerization technologies. 

1. **Layered Structure**: It consists of several layers, each layer is a filesystem that can be read-only or read-write. These layers are stacked on top of each other.

2. **Unified View**: To the user or application, the union filesystem appears as a single filesystem. Files and directories from all layers are presented in a unified view. If the same file exists in multiple layers, the top-most layer's version is shown.

3. **Copy-on-Write (CoW)**: When a file from a read-only layer is modified, the union filesystem uses a technique called "Copy-on-Write". It copies the file to a writable layer and then makes the changes. This way, the original file remains unchanged in the read-only layer.

Popular implementations of union filesystems include OverlayFS and AUFS

![Image layers](https://coolshell.cn/wp-content/uploads/2015/08/docker-filesystems-busyboxrw.png)

### Converting a running container into an image

We started a running container using ubuntu:latest image
`docker run --name hw_container ubuntu:latest touch /helloworld`

From this container, we created an image
`docker commit hw_container hw_image`

Similarly, we created an Ubuntu container packaged with 'Git'

`docker run -it --name image-dev ubuntu:latest /bin/bash`

`apt-get update && apt install -y git`

The following command showed all the differences between the base image and the latest layer.
`docker diff image-dev`

'-a' represent the author and '-m' represents the commit message.
`docker commit -a "@Alap" -m "Added Git" image-dev ubuntu-git`

`docker inspect image-dev`

An entrypoint is the program that will be executed when the container starts. We set entrypoint for the above container to git.

`docker run --name cmd-git --entrypoint git ubuntu-git`

We overwrote the ubuntu-git image w/ the new layer.
`docker commit -a "@Alap" -m "Set CMD to git" cmd-git ubuntu-git`

Test-drive new Image
`docker run --name cmd-git ubuntu-git version`

### Environment Variables

Key-value pairs defined at terminal with '=' operator. NOTE: No space before or after the '=' operator.

`docker run --name rich-image-example -e ENV_EXAMPLE1=Rich -e ENV_EXAMPLE2=Example busybox:latest`

If you want to persist an environment variable between terminal restarts, you can store it in the file that is loaded with the terminal start (e.g. ~/.bashrc for user in Ubuntu)

The above 2 environment variables have added a new layer on top of busybox.

`docker run --name rich-image-example-2 --entrypoint "/bin/sh" rie -c "echo \$ENV_EXAMPLE1 \$ENV_EXAMPLE2"`


## Docker filesystem exploration

Each time a change is made to a union filesystem, that change is recorded on a new layer on top of all of the others.
Like additions, both file changes and deletions work by modifying the top layer. When a file is deleted, a delete record is written to the top layer, which hides any versions of that file on lower layers. When a file is changed, that change is written to the top layer, which again hides any versions of that file on lower layers. The changes made to the filesystem of a container are listed with the docker container diff command you used earlier.
When a file in a read-only layer (not the top layer) is modified, the whole file is first copied from the read-only layer into the writable layer before the change is made. This has a negative impact on runtime performance and image size.
Images are stacks of layers constructed by traversing the layer dependency graph from a starting layer. 

## Docker tags

Used to identify an image.

`docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`


### Dockerfile
[Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

The default and most common name for a Dockerfile is Dockerfile. However, Dockerfiles can be named anything because they are simple text files and the build command accepts any filename you tell it. Use -f flag if using a different name but also specify the location of the Dockerfile.

```
# An example Dockerfile for installing Git on Ubuntu
FROM ubuntu:latest
LABEL maintainer="dia@allingeek.com"
RUN apt-get update && apt-get install -y git
ENTRYPOINT ["git"]
```

`docker build -t ubuntu-git:auto .`

`docker run --rm ubuntu-git:auto version` - Gets the git version

FROM ubuntu:latest— Tells Docker to start from the latest Ubuntu image just as you did when creating the image manually.
LABEL maintainer— Sets the maintainer name and email for the image. Providing this information helps people know whom to contact if there’s a problem with the image. This was accomplished earlier when you invoked commit.
RUN apt-get update && apt-get install -y git— Tells the builder to run the provided commands to install Git.
ENTRYPOINT ["git"]— Sets the entrypoint for the image to git.


The docker image build command has another flag, --file (or -f for short), that lets you set the name of the Dockerfile. Dockerfile is the default, but with this flag you could tell the builder to look for a file named BuildScript or release-image.df. This flag sets only the name of the file, not the location. That must always be specified in the location argument.

```
FROM debian:buster-20190910
LABEL maintainer="dia@allingeek.com"
RUN groupadd -r -g 2200 example && \
    useradd -rM -g example -u 2200 example
ENV APPROOT="/app" \
    APP="mailer.sh" \
    VERSION="0.6"
LABEL base.name="Mailer Archetype" \
      base.version="${VERSION}"
WORKDIR $APPROOT
ADD . $APPROOT
ENTRYPOINT ["/app/mailer.sh"]      1
EXPOSE 33333
# Do not set the default user in the base otherwise
# implementations will not be able to update the image
# USER example:example
```

ENV, WORKDIR, ADD, EXPOSE, USER

ENV - Sets the environment variables in the Docker image created from the Dockerfile. Also, you can substitute the value of the environment variable in the rest of the Dockerfile.

WORKDIR - Sets the current working directory

ADD - Add local or remote files and directories to the image/container

EXPOSE - Describe which ports your application is listening on

USER - Sets the user for the docker image and for any layers above this image. Use with caution as only root user can install software

`docker build -t dockerinaction/mailer-base:0.6 -f mailer-base.df .`

The ENTRYPOINT instruction has two forms: the shell form and an exec form. The shell form looks like a shell command with whitespace-delimited arguments. The exec form is a string array in which the first value is the command to execute and the remaining values are arguments. 

![shell vs exec command](https://i.ytimg.com/vi/Si6r-KUE-Ds/maxresdefault.jpg)

A command specified using the shell form would be executed as an argument to the default shell. Most importantly, if the shell form is used for ENTRYPOINT, all other arguments provided by the CMD instruction or at runtime as extra arguments to docker container run will be ignored. This makes the shell form of ENTRYPOINT less flexible.

A Dockerfile defines three instructions that modify the filesystem: COPY, VOLUME, and ADD. 

Continue next class from 8.2.2.