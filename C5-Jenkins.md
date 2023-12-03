# Class 5 - Dec' 2, '23 - Jenkins

## Introduction
![Jenkins Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Jenkins_logo.svg/1200px-Jenkins_logo.svg.png)

> Jenkins is the greatest CI/CD tool of all time.

---

# Introduction

> SDLC - Sofware Development Lifecycle

2 main -> Waterfall and Agile

![Waterfall vs Agile](https://jdmeier.com/wp-content/uploads/2023/03/Waterfall-vs.-Agile.jpg)

Jenkins helps us with implementing Agile methadology.

### Key Concepts

Continuous Integration (CI) - The practice of automating the integration of code changes from multiple contributors into a single software project. 

Continuous Delivery (CD) - A software development practice where code changes are automatically built, tested, & ready for release to production.

Continuous Deployment (CD) - With continuous deployment, production happens automatically without explicit approval. 

![CD vs CD](https://d1.awsstatic.com/product-marketing/DevOps/continuous_delivery.4f4cddb8556e2b1a0ca0872ace4d5fe2f68bbc58.png)

# Installing Jenkins

Prerequisite: Java 11 or 17 for 2.361.1 (LTS)

What are the 2 things you can install to get Java onto your machine?

JDK -> Java Development Kit

JRE -> Java Runtime Environment

Check for installed package in Linux:
dpkg - Debian Package manager `dpkg -s | grep <package_name>` 
rpm - Red Hat Package manager `rpm -qa | grep {package-name}`

JRE did not come with a compiler and JDK comes with it (javac).

Installed Jenkins on an Ubuntu server by copying script from jenkins.io/download and ran as a shell script.
We also saw that Jenkins is distributed as a .WAR file and can be run with JVM.

We checked port that Jenkins was listening on `ps -ef | grep Jenkins` or `ss -tulpn`

We went to the site on the browser using the above IP and input the default password. Then, we installed suggested plugins and then created a local 'admin' user.

# Creating a node

1. Installed JAVA (JDK 17) on the Jenkins agent node virtual machine.

2. On another VM, we started by creating a user named 'jenkins' with '/home/jenkins' as a home directory
`useradd -m -d /home/jenkins Jenkins`

3. Generate an ssh-keypair on the controller machine & the Jenkins agent node.

4. Copied the public key to the Jenkins agent node.
`ssh-copy-id <user>@<IP>`

5. From GUI, Dashboard -> Manage Nodes -> Nodes

Enter Node name & set as Permanent agent

Number of executors depends upon the CPU count and whether the application is multi-threaded.

Labels -> metadata about the Nodes

Launch method -> Launch Agents via SSH -> HOST (IP address of the node) -> Credentials (add creds to the Jenkins Credentials Provider) -> If using Private key, use the Controller's private key -> Manually trusted Key verification strategy

# Manage Jenkins

General Jenkins options available here.

# Freestyle Jobs

OG way of working with Jenkins.

# Pipeline
 
[Pipelines are the preferred methadology.](https://www.jenkins.io/doc/book/pipeline/#why)

2 ways of defining a Jenkinsfile

1. Declarative approach (preferred)

2. Scripted pipeline (Imperetive approach)

Agent -> Any, Label block, & none

Jenkinsfile -> starts w/ Pipeline -> agents -> stages -> stage('name') -> steps

Most operating methadology will be with connecting to SCM (Source Code Management). We connected our Jenkins instance to GitHub using an SSH keypair.

We can have webhook -> GitHub will trigger the pipeline every time there is a change to the repo on the specified branch.

Pipelines can be triggered manually, cron job, Poll SCM at regular intervals.

We dived into Java web applications -> Spring framework -> start.spring.io -> Downloaded a package -> We used maven to run the application `mvn spring-boot:run`

![Jenkins workflow](https://www.jenkins.io/images/pipeline/jenkins-workflow.png)
---

### Homework

1. Connect GitHub Repo to Jenkins
2. Connect a Jenkins agent using SSH keypair authentication
3. https://www.jenkins.io/doc/tutorials/ (Hold on till next week's class)
