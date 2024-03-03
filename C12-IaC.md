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

1. Automation: Automates the deployment of infrastructure, reducing the potential for human error and increasing efficiency.
2. Consistency: Ensures consistent environments are created every time, eliminating the "it works on my machine" problem.
3. Reusability: Allows for the reuse of code for setting up infrastructure, saving time and effort in the process.
4. Version Control: Infrastructure can be versioned and tracked using the same version control systems (like Git) as application code, making it easier to manage changes and rollbacks.
5. Cost Reduction: Reduces the cost associated with manual setup and maintenance of infrastructure.
6. Speed: Significantly speeds up the process of provisioning and scaling infrastructure, enabling faster development cycles.
7. Documentation: Acts as a form of documentation, showing exactly how the infrastructure is set up.

## Vagrant

Vagrant is a powerful tool for managing virtual machine environments in a single workflow. It provides an easy-to-use workflow and automation for setting up and managing virtual machines (VMs).

Pre-requisites:

1. VirtualBox
2. Vagrant

Create a directory for your Vagrant project. This directory will contain all the files related to your VM.

```bash
mkdir my_vagrant_project
cd my_vagrant_project
```

NOTE: The following 'init' commands might fail - run the following commands in order to fix the issue:
`vagrant plugin expunge --reinstall`
`vagrant plugin update`

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

The following commands are self explanatory:

`vagrant suspend`
`vagrant resume`
`vagrant halt`
`vagrant destroy`
`vagrant box update`

You can configure multiple VMs in a single Vagrantfile for more complex environments.

Vagrant supports automatic provisioning with shell scripts, Ansible, Chef, and Puppet, allowing you to automatically install software and configure your VM upon provisioning.

Install a web server along with the VM:

1. Create a shell script file - refer to 'install_apache.sh'
2. Update the Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "MyUbuntuVM"
    vb.memory = "1024"
  end
  config.vm.network "forwarded_port", guest: 80, host: 8080
  # Provision with a shell script
  config.vm.provision "shell", path: "install_apache.sh"
end
```

3. `vagrant reload --provision` or `vagrant up`

---

## Terraform

<p align="center">
    <img src="https://i0.wp.com/build5nines.com/wp-content/uploads/2023/11/hashicorp-terraform-workflow-learn-build5nines.jpg" style="width:600px;"/>
</p>

To deploy infrastructure with Terraform:

Scope - Identify the infrastructure for your project.
Author - Write the configuration for your infrastructure.
Initialize - Install the plugins Terraform needs to manage the infrastructure.
Plan - Preview the changes Terraform will make to match your configuration.
Apply - Make the planned changes.

[Install Terraform from the documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)


### HCL

A block has a type. Each block type defines how many labels must follow the type keyword. 

After the block type keyword and any labels, the block body is delimited by the { and } characters.

### Provider

Terraform relies on plugins called providers to interact with cloud providers, SaaS providers, and other APIs.

Terraform configurations must declare which providers they require so that Terraform can install and use them. Additionally, some providers require configuration (like endpoint URLs or cloud regions) before they can be used.

### Sample workflow

We created the 'terraform' block and the 'provider' blocks.

Then, we created the resource block, 'google_compute_instance'.

We have Google Cloud SDK installed on our machine, to authenticate to GCP using our account, we used the `gcloud auth application-default login` command.

1. `terraform init`: Initialize a Terraform working directory.
2. `terraform plan`: Show changes required by the current configuration.
3. `terraform apply`: Apply the changes required to reach the desired state of the configuration.
4. `terraform destroy`: Destroy the Terraform-managed infrastructure.
5. `terraform state list`: Lists the resources currently managed by Terraform

### Authenticating using Service Account JSON

> Important NOTE: NEVER EVER EVER put your service account json in your code repository and push to remote repo

We created a Service account, then, created a key-pair for the service account and stored in locally as a .json file.

Then, exported the key location as an environment variable.

```bash
export GOOGLE_APPLICATION_CREDENTIALS='C:\Users\user\Desktop\red-grid.json'

$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\user\Desktop\red-grid.json"
```

In production, the json variables would be stored in the CI/CD tools under variables as a secret.

### Variables

Sometimes, we want to re-use the same resources across different environments, for this, we can leverage variables.

We first create a variable block that defines the name of the variable.

```bash
variable "availability_zone_names" {
  type    = list(string)
  default = ["us-west-1a"]
}
```

[Varible Types] (https://developer.hashicorp.com/terraform/language/expressions/types)

string: a sequence of Unicode characters representing some text, like "hello".
number: a numeric value. The number type can represent both whole numbers like 15 and fractional values like 6.283185.
bool: a boolean value, either true or false. bool values can be used in conditional logic.
list (or tuple): a sequence of values, like ["us-west-1a", "us-west-1c"]. Identify elements in a list with consecutive whole numbers, starting with zero.
set: a collection of unique values that do not have any secondary identifiers or ordering.
map (or object): a group of values identified by named labels, like {name = "Mabel", age = 52}
null: a value that represents absence or omission. If you set an argument of a resource to null, Terraform behaves as though you had completely omitted it — it will use the argument's default value if it has one, or raise an error if the argument is mandatory. null is most useful in conditional expressions, so you can dynamically omit an argument if a condition isn't met.
Literal Expression

Value for the variable can be provided through the CLI:

`terraform plan -var availability_zone_names=["us-west-1a", "us-west1-b"]`

Or, if you have a lot of variables, better to put them all in a separate 'variables.tf' file and then create another file for their value based on environments -> e.g. dev.tfvars

`terraform plan -var-file dev.tfvars`

Terraform loads variables in the following order, with later sources taking precedence over earlier ones:

Environment variables
The terraform.tfvars file, if present.
The terraform.tfvars.json file, if present.
Any *.auto.tfvars or *.auto.tfvars.json files, processed in lexical order of their filenames.
Any -var and -var-file options on the command line, in the order they are provided. (This includes variables set by a Terraform Cloud workspace.)

### Modules

Terraform modules are containers for multiple resources that are used together. A module can include resources from the same provider or multiple providers. Modules in Terraform are used to encapsulate and reuse code, to organize Terraform configurations into logical components, and to facilitate code sharing between projects or teams.

You have root modules and child modules.

### Using Modules:

To use a module in your Terraform configuration, you specify a `module` block with the source of the module and any required input variables. Here's a basic example:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true
}
```

In this example, the `module` block tells Terraform to use the AWS VPC module from the Terraform Registry, specifying the version and various input variables required by the module.

### GCP Compute Instance example for Tf Moduless

Creating a simple Terraform module for deploying a Google Compute Instance involves two main parts: defining the module itself and then using that module in your Terraform configuration. Below is a step-by-step guide to creating a basic module for a Google Compute Instance.

### Step 1: Define the Module

1. **Create a Directory for Your Module**: Modules are organized in directories. Create a directory for your module, e.g., `google_compute_instance_module`.

    ```bash
    mkdir google_compute_instance_module
    ```

2. **Add a `main.tf` File**: Inside this directory, create a `main.tf` file. This file will contain the definition of the Google Compute Instance resource.

    ```hcl
    # google_compute_instance_module/main.tf

    resource "google_compute_instance" "vm_instance" {
      name         = var.instance_name
      machine_type = var.machine_type
      zone         = var.zone

      boot_disk {
        initialize_params {
          image = var.image
        }
      }

      network_interface {
        network = "default"
        access_config {
          // Ephemeral IP
        }
      }
    }
    ```

3. **Add a `variables.tf` File**: Define the necessary variables for your module. Create a `variables.tf` file in the same directory.

    ```hcl
    # google_compute_instance_module/variables.tf

    variable "instance_name" {
      description = "The name of the instance"
      type        = string
    }

    variable "machine_type" {
      description = "The machine type of the instance"
      type        = string
    }

    variable "zone" {
      description = "The zone where the instance will be created"
      type        = string
    }

    variable "image" {
      description = "The image to use for the instance's boot disk"
      type        = string
    }
    ```

4. **Add an `outputs.tf` File** (Optional): If you want your module to output certain values, such as the instance's IP address, create an `outputs.tf` file.

    ```hcl
    # google_compute_instance_module/outputs.tf

    output "instance_ip" {
      value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
    }
    ```

### Step 2: Use the Module in Your Configuration

1. **Create a Terraform Configuration File**: In your project's root directory (not inside the module directory), create a `main.tf` file where you'll use the module.

    ```hcl
    provider "google" {
      credentials = file("<YOUR-CREDENTIALS-FILE>.json")
      project     = "<YOUR-PROJECT-ID>"
      region      = "us-central1"
    }

    module "google_compute_instance" {
      source       = "./google_compute_instance_module"
      instance_name = "test-instance"
      machine_type = "e2-micro"
      zone         = "us-central1-a"
      image        = "debian-cloud/debian-9"
    }
    ```

    Replace `<YOUR-CREDENTIALS-FILE>.json` and `<YOUR-PROJECT-ID>` with your actual GCP credentials file path and project ID.

2. **Initialize Terraform**: Run `terraform init` to initialize the Terraform project, which will download the Google provider and prepare your module.

3. **Apply Your Configuration**: Execute `terraform apply` to create the resources defined in your module. Confirm the action when prompted.

---