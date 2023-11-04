# Class 2 - November 4, 2024 - Linux

## Introduction
![Tux - The Linux Penguin](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)

> Linux is the greatest operating system of all time.

---

## 1 - Few more basic Linux commands

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

