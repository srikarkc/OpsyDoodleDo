# Class 9 - Jan' 27, '24 - Kubernetes

## Introduction
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Kubernetes_logo.svg/2560px-Kubernetes_logo.svg.png" alt="K8S Logo" style="width:300px;"/>

> Kubernetes is a container orchestrataion engine. 

<img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1671213280990/agVlGw_sl.png" alt="Helm Logo" style="width:600px;"/>

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

    In Kubernetes, Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) facilitate the management of storage independently of pod lifecycles. PVs are pre-provisioned or dynamically created storage units, offering various backends like NFS and cloud storage, with specific access modes and policies. PVCs allow users to request these storage resources without knowing underlying details, specifying size and access needs. Through a binding process, PVCs are matched with suitable PVs, ensuring that applications have the necessary storage, thereby abstracting and simplifying storage provisioning and management in a cloud-native environment.

---

## Helm Charts

### Apache Webserver

[https://httpd.apache.org/download.cgi](Apache Web Server)

1. Install as a service on a VM by following the instructions on the link above.

2. As an improvement to the workflow, we use Docker containers to run the webserver, easier to share and pass configuration.
    [https://hub.docker.com/_/httpd](httpd image on Docker Hub)
    ```
    docker pull httpd
    docker run -dit --name my-running-app -p 8080:80 httpd:latest
    ```

3. Change the index.html file to say, 'Welcome to the Hotdog site'.
    We create a Dockerfile and a custom image from it
    ```
    FROM httpd:latest

    RUN echo '<html><head></head><body><h1>Welcome to Hotdog site!</h1></body></html>' > /usr/local/apache2/htdocs/index.html
    ```
    ```
    docker build -t my-apache2 .
    docker run -dit --name my-running-app -p 8080:80 my-apache2
    ```

4. We can run this as a Pod on Kubernetes so that scaling is automatic and better. We can also leverage other Kubernetes features such as under-lying hardware abstraction, volumes, etc.
    For this, we need to push our image to the Docker Hub.
    `docker tag my-apache2 srikarkc/my-apache2:latest`
    `docker push srikarkc/my-apache2:latest`
    `kubectl run hotdog-site --image=srikarkc/my-apache2:latest --port=80`

    We can use a Deployment object instead of Pod - this will enable us to setup auto-scaling for the Pods.

5. BUT, we still are not sure whether we're using Apache the best way on the Kubernetes cluster. Maybe there are some better objects to use the webserver with on the Kubernetes cluster.

This is where Helm comes into the picture.

    1. First, we [https://helm.sh/docs/intro/install/](install helm)
    2. We check Artifact Hub for the Chart Repository
    3. We add the chart repository
        `helm repo add bitnami https://charts.bitnami.com/bitnami`
    4. We install using the following command:
        `helm install my-apache bitnami/apache --version 10.5.4`

6. Now that we used the Helm chart, we want to customize values there so we will create and use a file called 'custom-values.yaml'
    ```
    # custom-values.yaml
    image:
        registry: docker.io
        repository: srikarkc/hotdog-site
        tag: latest
        pullPolicy: IfNotPresent
    ```
    `helm install my-apache bitnami/apache --version 10.5.4 -f custom-values.yaml`

---