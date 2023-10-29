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

5. Find the current Operating system

`uname -a` or `hostnamectl`

---

## 4 - File Hierarchy Structure

![Linux file hierarchy](https://www.tecmint.com/wp-content/uploads/2013/09/Linux-Directory-Structure.jpeg)

https://www.youtube.com/watch?v=HbgzrKJvDRw&ab_channel=DorianDotSlash

1. /etc -> It contains the system-wide configuration files.

2. /root -> Home directory for the root user.

3. /home -> Contains the user account home directories.

4. /tmp -> Can be used for temporary files and scp(ing) files here. Will be deleted at start. Can be accessed by all users.

5. /proc -> Can be used to find system information. (e.g. cat /proc/[uptime|cpuinfo])

---

## 5 - Crontab

When you want to schedule a task for a certain period of time -> you can use crontab.

	a. Go to crontab.guru to find the schedule that you want.
	b. Add your job to crontab list for the current user by `crontab -e'
	c. List the current crontab jobs by `crontab -l`

---

## 6 - Logical Volume Manager
![LVM image](https://www.brainupdaters.net/wp-content/uploads/2017/01/LogicalVolumenManager.jpg)

	1. Add a disk
		`lsblk`
	2. Create a partition
		`fdisk` -> n -> +10G -> w
	3. Create a Physical Volume and list them
		`pvcreate /dev/sdb1` and `pvs`
	4. Create a Volume Group and list them
		`vgcreate drive_two /dev/sdb1` and `vgs`
	5. Create a Logical Group and list them
		`lvcreate -L 9G -n mylv drive_two` and `lgs`
	6. Make a new filesystem (XFS)
		`mkfs.xfs /dev/sdb/sdb1/drive_two-mylv`
	7. Mounted the filesystem
		`echo "/dev/drive_two/mylv     /home/avyas             xfs     defaults                     0 0" >> /etc/fstab`
	8. Check disk usage
		`df -h`
![Mount options](https://www.cyberpratibha.com/wp-content/uploads/2020/06/use-of-fstab-option-for-mounting-disk-in-linux-File-System-Table-fstab-Entry-Explained.png)


	9. Extend logical Volume by using storage from vg
		`lvextend -L +9.9G /dev/drive_two/mylv -r`
		Make sure you remember the '-r' option!
		or you can use 100% of the new physical Volume
		`lvextend /dev/drive_two/mylv /dev/sdb2 -r`


BONUS -> Create a large file `dd if=/dev/urandom of=5gbfile bs=1M count=5120`
---

## 6 - System administrative tasks

1. Package management
	a. How to install packages? 
	b. How to start them up at runtime?

`subscription-manager register --username <username> --password <password> --auto-attach`

`yum update`

`yum [search|install] <name_of_the_package>`

`systemctl [start|status|stop|enable|disable] <service_name>`

`systemctl status firewalld`

`firewall-cmd --list-all`

`firewall-cmd --add-service http --permanent && firewall-cmd --reload`

3. Changing the static IP of a system & also brief look at the system firewall

`vi /etc/sysconfig/network-scripts/ifcfg-<ethernet_device_name>`
-> Make sure the BOOTPROTO=static and IPADDR

---

# NOTES:

### Go to Red Hat developer website and create a developer account for yourself.

### Learn how to use vieditor from `vimtutor`

### All passwords in the class: Fortinet123#