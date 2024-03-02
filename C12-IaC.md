# Class 12 - March 2, '24 - IaC

<p align="center">
    <img src="https://media.licdn.com/dms/image/D4E12AQF87JaFit12eA/article-cover_image-shrink_600_2000/0/1686738865658?e=2147483647&v=beta&t=ytu7ACQOBlmrfRobY3RHvNX_ZMM5Jmh9f986AgXQ0Wg" style="width:600px;"/>
</p>

> Terraform is an open-source Infrastructure as Code (IaC) tool that allows users to define and provision data center infrastructure using a high-level configuration language.
---

## Introduction

Infrastructure as Code (IaC) is a key practice within the domain of DevOps and cloud computing, which involves managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. 

This approach allows developers and IT operations teams to automatically manage, monitor, and provision resources through code, rather than using a manual process.

The core benefits of IaC include:

Automation: Automates the deployment of infrastructure, reducing the potential for human error and increasing efficiency.
Consistency: Ensures consistent environments are created every time, eliminating the "it works on my machine" problem.
Reusability: Allows for the reuse of code for setting up infrastructure, saving time and effort in the process.
Version Control: Infrastructure can be versioned and tracked using the same version control systems (like Git) as application code, making it easier to manage changes and rollbacks.
Cost Reduction: Reduces the cost associated with manual setup and maintenance of infrastructure.
Speed: Significantly speeds up the process of provisioning and scaling infrastructure, enabling faster development cycles.
Documentation: Acts as a form of documentation, showing exactly how the infrastructure is set up.

## Vagrant

Vagrant is a powerful tool for managing virtual machine environments in a single workflow. It provides an easy-to-use workflow and automation for setting up and managing virtual machines (VMs).

Pre-requisites:
1. VirtualBox
2. Vagrant

Create a directory for your Vagrant project. This directory will contain all the files related to your VM.

```
mkdir my_vagrant_project
cd my_vagrant_project
```

Use the `vagrant init` command to create a new Vagrantfile in your project directory. The Vagrantfile is a Ruby file used to configure Vagrant environments.

`vagrant init`

To initialize a project with a specific box (a pre-packaged VM image), specify the box name. For example, to use an Ubuntu 20.04 box:

`vagrant init ubuntu/focal64`

Open the `Vagrantfile` in your favorite text editor to make configurations. Here's a simple configuration that specifies the use of VirtualBox and forwards a port from the guest VM to the host machine:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "MyUbuntuVM"
    vb.memory = "1024"
  end
  config.vm.network "forwarded_port", guest: 80, host: 8080
end
```

This configuration sets up an Ubuntu 20.04 VM with 1 GB of RAM and forwards port 80 from the VM to port 8080 on your host machine.

Use the `vagrant up` command to start your VM. This command reads the `Vagrantfile`, downloads the box if it's not already downloaded, and configures the VM according to your specifications.

`vagrant up`

Once the VM is up and running, you can SSH into it using:

`vagrant ssh`

This command provides you with a secure shell session inside your VM.

If you want to pause your VM and resume it later, use:

`vagrant suspend`
`vagrant resume`
`vagrant halt`
`vagrant destroy`
`vagrant box update`

You can configure multiple VMs in a single Vagrantfile for more complex environments.

Vagrant supports automatic provisioning with shell scripts, Ansible, Chef, and Puppet, allowing you to automatically install software and configure your VM upon provisioning.

