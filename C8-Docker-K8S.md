# Class 8 - Jan' 13, '24 - Docker and Kubernetes

## Introduction
![Docker Logo](https://www.docker.com/wp-content/uploads/2023/08/logo-dont-spacing.svg)

> Docker is a platform for running applications in lightweight containers. Kubernetes is a container orchestrataion engine.

---

### Revision

We create a Flask Python project, then, we wrote a Dockerfile. We built an image from this file and pushed it to Docker Hub. We tested the project by running it on a VM.

### Docker in production

Development team would push the application code to the remote repository. This will trigger a build on the Ci/Cd platform (e.g. Jenkins) creating an artifact. This artifact will be integrated in the Dockerfile which will be used to create a Docker image. This Docker image will be pushed to a private registry (e.g. Docker Hub, ECR, GCR, Harbour). Then, in the deployment stage, the server will pull the image from the private registry and run them.

### Docker compose

Docker Compose is a tool for defining and running multi-container Docker applications.

1. **Configuration**: With Compose, you use a YAML file to configure your application’s services, networks, and volumes. This file is typically named `docker-compose.yml`.

2. **Simplicity and Efficiency**: It simplifies the deployment of multi-container applications. Instead of running multiple commands to set up each container, you run a single command that does it all based on your configuration.

3. **Development-Production Parity**: Compose ensures your application runs the same in different environments, such as development, staging, and production. This is crucial for testing and reliability.

4. **Service Management**: It manages the entire lifecycle of your application – starting, stopping, and rebuilding services, viewing the status of running services, streaming log output of running services, etc.

5. **Networking**: Compose sets up a single network where your containers can communicate with each other. This network is isolated from other networks on your host.

6. **Volumes and Data Persistence**: It can be used to manage volumes for data persistence and share data between containers.

```
version: '3.8'

services:
  frontend:
    image: node:latest
    volumes:
      - ./frontend:/usr/src/app
    working_dir: /usr/src/app
    ports:
      - "3000:3000"
    command: npm start
    depends_on:
      - backend

  backend:
    image: python:3.8
    volumes:
      - ./backend:/usr/src/app
    working_dir: /usr/src/app
    ports:
      - "5000:5000"
    command: python app.py
    depends_on:
      - db

  db:
    image: postgres:latest
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: example
    ports:
      - "5432:5432"

volumes:
  pgdata:
```
