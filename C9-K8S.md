# Class 9 - Jan' 20, '24 - Kubernetes

## Introduction
![K8S Logo](https://www.docker.com/wp-content/uploads/2023/08/logo-dont-spacing.svg)

> Kubernetes is a container orchestrataion engine.

---

### Pod

You can create a Pod either from CLI or with a YAML configuration file.

`kubectl run my-k8s-py-app --image=srikarkc/my-hello-python-app:v2`

We can generate the yaml definition file from the CLI.

`kubectl run hello-world --image=hello-world --dry-run=client -o yaml > hello-world.yaml`

[More yaml definition shortcuts](https://devopscube.com/create-kubernetes-yaml/)


### Labels

Labels in Kubernetes are key-value pairs attached to objects, such as pods, services, and deployments. They are used to organize and select a subset of objects, based on the requirements.


### Namespaces

Kubernetes namespaces are a key feature for organizing and isolating cluster resources. Namespaces provide a scope for names, allowing the same resource names to be used in different namespaces. Common use cases include separating environments (development, staging, production), differentiating teams or projects, and managing resource quotas. While they offer a level of isolation, namespaces do not provide strong security boundaries.


### Liveness Probe

When you run a container in a Pod and the container crashes, kubelet brings up the container for us. Sometimes, our application may become unresponsive without the PID 1 (main process) crashing. In this case, we need a way to check whether our application is responsive and the container/Pod needs to be restarted. For this, Kubernetes provides a Liveness probe feature w/ 3 types of probes.

1. HTTP GET
2. TCP Socket
3. Exec probe (status code 0)

You can configure additional properties such as timeout, delay, failures, & period.


### Replication Controllers

They control the number of replicas of a Pod as defined in your Deployment yaml file.

They have 3 main parameters which are:
1. Label selector,
2. Replica count,
3. Pod template

Replication Controller use Label selectors for Pods.


### Replica Sets

A ReplicaSet behaves exactly like a ReplicationController, but it has more expressive pod selectors. Whereas a ReplicationController’s label selector only allows matching pods that include a certain label, a ReplicaSet’s selector also allows matching pods that lack a certain label or pods that include a certain label key, regardless of its value.


### Daemon Sets

When you need to run exactly 1 Pod on each on the nodes in the cluster.
e.g. a log collector and a resource monitor


### Jobs & CronJobs

Allow you to run a pod whose container isn’t restarted when the process running inside finishes successfully. Once it does, the pod is considered complete.

A CronJob creates Jobs on a repeating schedule.

CronJob is meant for performing regular scheduled actions such as backups, report generation, and so on. 


### Deployments

A Kubernetes Deployment is a resource object in Kubernetes that provides declarative updates to applications. It allows you to describe an application’s desired state, such as which images to use and the number of pod replicas. The Deployment controller changes the actual state to the desired state at a controlled rate, managing and updating instances of your application. 

Deployments are ideal for stateless applications and support zero-downtime updates, rollback, and scaling. They are crucial for maintaining the reliability and availability of applications, ensuring that a specified number of pods are always running and deploying new versions progressively.


---

## Services

There are 3 major types to expose a service running in a Pod:
1. ClusterIP,
2. NodePort, &
3. LoadBalancer
4. Ingress

### ClusterIP

Pods like many things in life, come and go. Each Pod has its own IP address (ephemeral), we need a way to reliably access services on a Pod.

ClusterIP provides a static IP address which gets mapped to Pods based on their labels. These labels are defined in the Pod definitions and under selector in the service definition.

Kubernetes creates an endpoints object which keeps a track of which Pods are the members of a service.








### Side Bar

Learn how to use json query (jq).
`kubectl get pods -o json | jq '.items[0].metadata.namespace'`

Today's topics - Services, & Volumes

Next meet - App Mesh, Helm

---

# Homework

[Create K8S Cluster from Scratch](https://github.com/kelseyhightower/kubernetes-the-hard-way)

[Kubernetes networking explained](https://www.tigera.io/learn/guides/kubernetes-networking/)

### To-Do:

1. First deploy Jenkins instance. 
2. Connect Code Repository w/ Jenkins.
3. Every new commit to the master branch should trigger a new build.
4. Use the python-portfolio-app and then run a test (using the Django testing framework).
5. Package the python app.
6. Create a Docker image using the Dockerfile and above artifact.
7. Push image to Google Artifact Registry.
8. On a K8S cluster running in GKE, pull the above image and deploy to production.
9. Create/update service to expose the above application externally.
