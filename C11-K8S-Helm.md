# Class 9 - Jan' 27, '24 - Kubernetes

## Introduction
![K8S Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Kubernetes_logo.svg/2560px-Kubernetes_logo.svg.png)

> Kubernetes is a container orchestrataion engine. 

![Helm Logo](https://cdn.hashnode.com/res/hashnode/image/upload/v1671213280990/agVlGw_sl.png)

> Helm is a package manager for Kubernetes that simplifies the deployment and management of applications on Kubernetes clusters.
---

## Volumes

1. By default, the filesystem for a container is based on its layers. Any changes made are made at the top-most layer of this filesystem.

2. Sometime, we want to share data between containers, we can do this by using Docker volumes.

    `docker run -d --mount source=my-vol,target=/tmp ubuntu:latest`

3. 