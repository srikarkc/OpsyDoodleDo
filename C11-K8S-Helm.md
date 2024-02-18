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

3. We wanted to share files between two pods. For this, we created a pod definition with volumes section. 

    ```
    volumes:
    - name: html
        emptyDir: {}
    ```

4. We mounted this volume in our pod definition for each container. 

5. To confirm this configuration is working, we did portforwarding and curled. 

    ```
    kubectl port-forward fortune 8080:80
    curl http://localhost:8080
    ```

6. Now, in case of kubrnetetes, a pod generally runs one container. However, in some cases, you may need more than one container in a pod. The second container may serve a secondary purpose such as log collection. This secondary container can be called a sidecar container. 

7. There are several ways to share storage between pods in Kubernetes. We first covered EmptyDir. 

    ```
    volumes:
    - name: html
      emptyDir: {}
    ```
8. In this example, we mounted an Empty directory named HTML in the container in pod's definition.

    ```
    containers:
    - image: srikarkc/fortune
      name: html-generator
      volumeMounts:
      - name: html
        mountPath: /var/htdocs
    - image: nginx:alpine
      name: web-server
      volumeMounts:
      - name: html
        mountPath: /usr/share/nginx/html
        readOnly: true
    ```

9. EmptyDir does not persist storage. So, we looked at PV and PVC. 

    <img src="https://blog.mayadata.io/hubfs/Storageclass%20blog%20%281%29-1.png" alt="PV and PVC" style="width:400px;"/>