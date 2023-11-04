# Class 2 - November 4, 2024 - Linux

## Introduction
![Tux - The Linux Penguin](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)

> Linux is the greatest operating system of all time.

---

## 1 - Few basic Linux commands

![Wild card characters](https://res.cloudinary.com/practicaldev/image/fetch/s--mat5AjJs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/vnxp1uywkv4ct9g5vdqy.png)

? & * -> Match single character and multiple character

ls <file> | grep -A \[number] -B \[number] -> Shows you lines above and below a number

>, >> , <, & | -> Re-direct operators

![Operators](https://media.cheatography.com/storage/thumb/davechild_linux-command-line.750.jpg?last=1582977076)

Basic variables -> `COLOR=blue` (Remember no space around =) & value `echo $COLOR`

### Running scripts

1. Convention to name scripts ending with '.sh'.

2. First line -> `#!/bin/bash`

3. Add permission to execute the script. `chmod +x script-name.sh`

4. Run the script by putting either absolute or relative path to the script. `./script-name.sh`

5. PATH variables is a list of locations where the system knows to run the programs from. If you have the script on a location in on of the $PATH locations, you can run just the name of the script -> `script-name.sh`.

### STDIN, STDOUT, STDERR

1. Programs need to access the data from memory.

2. Programs use operating system's primitive functions to refer to the data, and the operating system will map to that data in memory using file descriptor. 

3. The file descriptor for STDIN = 0, STDOUT = 1, STDERR = 2 

4. You'd check the output of the program's return code using `echo $?`

5. You'd use > and 2> redirect operators to direct return code to a file. 

### Job Control

1. Long running command -> `ping google.com`

2. Stop the program and move to background -> Ctrl+Z

3. Check current user processes -> `ps`

4. Bring it back to foreground -> `fg <program name>`

5. Kill the process -> `kill -9 <PID>`

[Kill signals](https://www.cyberciti.biz/faq/unix-kill-command-examples/)

6. When a process is stopped -> You get a job -> See jobs with `jobs`

7. Start the job again -> `fg %<job_id>`

### Top command

1. Load Average -> provides a measure of demand on system CPU and disk I/O -> (1, 5, & 15 minutes average)

2. Sleeping processes -> Processes that are currently blocked waiting for some event or condition to occur before they can continue executing.

	Daemon process -> Daemon processes are long-running background processes that perform system-related tasks or provide services independently of user interaction.
	
	Zombie process -> Parents didn't listen to the child's return code and thus they still exist in the process tree after they have completed execution.
	
3. Niceness -> Higher values have lower priority.

4. Sort by CPU -> 'P' by Memory -> 'M'

5. Display specific user processes -> 'u' -> username

6. Kill -> 'k' + PID + interrupt signal (e.g. 9 for kill)


---

## 2 - User management BASH script

1. We use the `echo` command to send messages to the terminal.
NOTE: When we mention the usage, `$0` means the name of the first and then `$1` is the first command line argument after the filename and so forth.
	```
	./user-management.sh add alap
	```
	
	**NOTE:**
	
	$0 - ./user-managment.sh  (the file name)
	$1 - add (the first argument - command)
	$2 - alap (second argument - username)
	
2. We create functions for each functionality.
	```
	add_user() {
		local username="$1"
		sudo useradd $username
		echo "User $username added successfully!"
	}
	```
	
3. We added case commands for specifying what kind of action to perform.
	```
	command="$1"
	username="$2"
	
	case "$command" in
		add)
			add_user "$username"
			;;
		*)
			echo "Incorrect command"
			exit 1
			;;
	esac
	```
	
4. We can use the if;then .... else ... fi command for specifying conditions.
	```
	if id $username &> /dev/null; then
		echo "User $username exists"
	else
		echo "User $username does not exist"
	fi
	```
	**NOTE**: &> outputs both standard output and standard error
	
5. In order to list all users, we can use the for loop.
	```
	for user in $(cut -d: -f1 /etc/passwd); do
		echo $user
	done
	```
	**NOTE**: `/etc/passwd` is the file that contains the list of all users. cut is the command that is used to cut a portion of the list. `-d:` means delimited by the colon(:) symbol and `f1` means the first field of the delimited list.
	
---

## 3 - NFS Share Lab

1. NFS -> Network File Systems is a distributed file system protocol that allows remote clients to access files and directories over a network as if they were stored locally on the client's own machine.

![NFS network diagram](https://drive.google.com/file/d/15MzfAbMhHjyzJJQejCEOCcXnnhC3H_fX/view?usp=sharing)