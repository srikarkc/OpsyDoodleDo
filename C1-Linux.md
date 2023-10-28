# Class 1 - October 28, 2023 - Linux

## Introduction
![Tux - The Linux Penguin](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)

> Linux is the greatest operating system of all time.

---


## 1 - Installing  Operating Systems

Download compatible image file. Compatible w/ the Hardware.
Linux is NOT an operating system. Linux is a kernel.
Kernel -> Acts as a gate and a fence to the underlying hardware.

Operating System over the kernel

### Common distributions of Linux

Debian
Ubuntu -> Cannonical -> Ubuntu 16.04 LTS / 18 / 20 / 22.04.3 LTS

Red Hat -> RHEL (license) -> 6 / 7 / 8 / 9
CentOS -> CentOS Stream -> Stopped at 7
Fedora

Oracle Linux -> 8 (similar to RHEL 8)

### Installation process

In ESXi -> You have a host (physical server) with 4 vCPU and 16G memory
Now, can you create 5 VMs w/ 2 vCPU and 4G memory each? ABSOLUTELY! over-provisioning

NAT -> Computer will create a new network and your VM will have one 1 IP in that network and your host computer will have 1 IP in that network and connections to the internet will go through your host PC.

Bridge mode -> Same network as your host computer.

If you install RHEL 8 without a license/subscription -> You will not be able to install packages 

Manual Partition -> You need /root directory, /boot directory, & swap space

What is swap space? Space that the computer uses when it runs out of memory (RAM).

---

## 2 - SHELL

What is SHELL?
SHELL takes commands from the keyboard and passes them to the operating system.

SHELL also helps you interpret the commands and special characters.

cd .   - current directory
cd ..  - parent directory
cd ~   - tilda - home directory
cd -   - back to the previous directory (jump)

### Create a user and change password

`useradd <user_account>`
`passwd <user_account>`

### If you don't have privileges to run a command, you need to either switch to the root user and run the command or use sudo before the command.

You need to be on the sudoers list to be able to run sudo commands.

add members to the wheel group: `usermod -aG wheel  <user_name>`

The gold standard way -> As a root user, run 'visudo'
`avyas   ALL=(ALL)       ALL`
`avyas   ALL=(ALL)       NOPASSWD:ALL`

### Delete user

`userdel -r <user_name>`

### Remove user from a group

`gpasswd --delete user group`

---

## 3 - Basic Linux Commands

1. Absolute and relative paths

2. Less command (j - down, k - up)

3. User permissions (long format - ls -l)

4. Add permissions

![Linux Permissions](https://i.redd.it/vkxuqbatopk21.png)

`chmod \[a+x|g-r|o+w|404] <file_name> to make the file readable to others.`

`groupadd <group_name>

`chmod -aG <group_name> <user_name>

`chown <user_name>:<group_name> <file_name>`

`gpasswd --delete user group`





---

# NOTES:

### All passwords in the class: Fortinet123#