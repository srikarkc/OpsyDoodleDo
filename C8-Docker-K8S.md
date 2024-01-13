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

---

# Kubernetes

### Introduction

Kubernetes primarily solves the problem of automating the deployment, scaling, and management of containerized applications across clusters of hosts.

### Control Plane components

The Kubernetes control plane consists of several key components, each with a specific role in managing the cluster:

1. **kube-apiserver**: This is the central management entity and API server for Kubernetes. It provides the Kubernetes API through which users, the different parts of the cluster, and external components communicate.

2. **etcd**: A highly available key-value store used as Kubernetes' backing store for all cluster data. It stores the entire state of the cluster at any given time, making it crucial for cluster state management and coordination.

3. **kube-scheduler**: Responsible for assigning newly created pods to nodes. It considers various factors such as resource requirements, hardware/software constraints, affinity and anti-affinity specifications, data locality, and workload-specific requirements.

4. **kube-controller-manager**: Runs controller processes, which are background threads that handle routine tasks in the cluster. These controllers include the Node Controller (for noticing and responding when nodes go down), Replication Controller (for maintaining the correct number of pods for every replication controller object), and others.

### Worker Plane Compoenents

1. **kubelet**: This is an agent that runs on each node in the cluster. It ensures that containers are running in a Pod and are healthy, based on the specifications provided in the PodSpecs.

2. **kube-proxy**: This network proxy reflects Kubernetes networking services on each node, maintaining network rules that allow network communication to your Pods from network sessions inside or outside your cluster.

3. **Container Runtime**: The software responsible for running containers. Kubernetes is agnostic to the container runtime, and it requires a container runtime for a node to work with containers. Examples include Docker, containerd, and CRI-O. 

---

### Hands-on

1. We installed Minikube on the Ubuntu VM which started a 'baby' K8S cluster for us for learning purposes which is running our local machine.

`minikube start`

2. We need to interact with this cluster so we installed 'kubectl' and kubectl configuration is pointing to the minikube cluster.

`kubectl cluster-info`
`kubectl get nodes`

3. 