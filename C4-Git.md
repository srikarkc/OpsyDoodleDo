# Class 4 - Nov' 25, '23 - Git

## Introduction
![Git Logo](https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png)

> Git is the greatest version control system of all time.

---

# Git - Stupid content tracker

> Git is a distributed versioning system

What does distributed mean?
Changes to the code are stored as a series of snapshots in local and can be reconciled with changes from other developers.

Distributed vs Centralized VCS
![VCS comparison](https://media.licdn.com/dms/image/C4D12AQFZL6KDlQruFg/article-inline_image-shrink_1000_1488/0/1615233466270?e=1704326400&v=beta&t=xsUo9SpQUxQ3cG_0-bnarbOmj-cHjpKbapYwICMcIyI)

### Workflow

1. Install Git

2. Initialize the directory - make it a git repository
`git init`

3. Add code to the repository

4. Status of Git
`git status`

5. Added our file to the staging area
`git add <filename>`
`git add .`

6. Committed the file
`git commit` - Opens up an editor and we typed the commit message and saved
`git commit -m "<commit message>"

7. List of commits
`git log`
`git log --oneline`

### Check differences

1. `git diff` - Difference between the current working directory state and the latest commit.

2. `git diff <hash1> <hash2>` - Compare between 2 commits

### Ignore files

Add a .gitignore file with the name of the files to ignore.

### Branch

1. Check which branch we're on
`git branch` or `git status`

2. Create a new Branch
`git branch <branch_name>`

3. Switch Branch
`git switch <branch_name>`

4. Delete Branch
`git branch -d <branch_name>`

5. Merge (simple fast-forward) - Switch to branch you want to merge into
`git merge <branch_name_of_the_branch_you_want_to_merge>`

6. Graph view for commit history
`git log --graph`

7. 3-way merge - When you have a 3 different versions to be merged.
	1. branch you're merging into version
	2. branch you have the changes version
	3. common version

![git 3-way merge](https://i.stack.imgur.com/96y6a.png)

### Stash

1. Put changes in the working directory away
`git stash` 
include tracked files (i.e. files in the staging area)
`git stash -u`
include ignored files
`git stash -a`

2. Bring the changes back to working directory and delete the Stash
`git stash pop`

### Tags
Like permanent bookmarks to reference specific commits.

Lightweight tags and annotated tags

Lightweight tags - Pointers to commit
`git tag <tag_name>`

Annotated tags - Stored as full objects in the Git database
`git tag -a <annotated_tag_name> -m <message>`

Annotated tags are meant for release while lightweight tags are meant for private or temporary object labels. For this reason, some git commands for naming objects (like git describe) will ignore lightweight tags by default.

### Git internals

Git works internally by managing a series of objects that represent the state of your project at various points in time. 

1. Repository: A Git repository is a directory that contains all the files and metadata necessary to track changes to your project. It includes the following components:
   - Working Directory: The working directory is where you edit and create files for your project. It contains the current state of your project.
   - Staging Area (Index): The staging area is an intermediate area where you prepare changes before committing them to the repository. You can selectively choose which changes to include in the next commit.
   - Object Database: The object database stores all the data required to represent the history of your project. Git uses a content-addressable file system, where objects are stored based on their content (SHA-1 hash).

2. Objects: Git manages objects as the fundamental building blocks of its internal data structure. There are four types of objects in Git:

   - Blob: A blob represents the content of a file at a specific point in time. It is a binary large object that stores the file's data.

   - Tree: A tree object represents a directory in your project. It contains references to blobs (files) and other tree objects (subdirectories). Trees organize the file hierarchy.

   - Commit: A commit object represents a specific snapshot of your project at a particular moment in time. It includes metadata such as the author, committer, timestamp, and a reference to the tree object representing the project's state.

   - Tag: A tag object is a reference to a specific commit. Tags are often used to mark specific points in history, such as software releases.

3. Branches are lightweight pointers to specific commits in the history. Git also maintains references like `HEAD` to track the currently checked-out branch or commit.

---

## Working with Remote Repositories

1. Created an account on a remote repository site (GitHub)

2. We created a new repository

3. Cloned it to our local
`git clone <HTTPS_link>`

4. List all remotes
`git remote -v`

5. Created and committed files. Then pushed the file.
`git push origin <branch_name>`

> Create pull requests after pushing code from working branch.

---

### Git Server

[Git Server Setup](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)

1. Installed git on the Server

2. Created a new user

3. Created a .ssh directory and copied the public key of the client to the authorized_keys file

4. Initialized a bare directory
`git init --bare`

5. Added remote on the client
`git remote add origin git@10.0.0.162:/home/git/git/project.git`

6. Push code to Remote
`git push origin master`

---

### Homework:

Find out how to delete old branches in local repository that are deleted in the remote repository.

git cherry-pick

Check how to delete a commit

[Git advanced commands](https://ohshitgit.com/)

Host a GitLab server