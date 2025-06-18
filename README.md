# Git Tutorial
This is a simple tutorial on how to use git. It covers the basics of git commands and workflows.


## Create a new repository

If you don't have a GitHub account, you can create one at https://github.com/join

After creating an account, you can create a new repository by clicking on the
"New" button on the repositories page.

Name the repository `git-tutorial` and add a description like "Alien species 
distribution". and make it public. 
Initialize the repository with a README file by checking the box "Add a README file"

## Install Git

### MacOS

To install Git on MacOS, you can use https://git-scm.com/downloads/mac

### Windows

To install Git on Windows, you can use https://git-scm.com/downloads/win

## Add new files

Clone the repository to your local machine using the following command 
(make sure to replace `USER-NAME` with your GitHub username):

```bash
git clone https://github.com/USER-NAME/git-tutorial
```

Go to the folder where you cloned the repository

Open a file editor and create a new file named `main/py` and add the contents from 
[main.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/main/main.py) to it.

Also create a new file named `select_habitat.py` and add the contents from 
[select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/main/select_habitat.py) to it.

Now you can add the files to the repository using the following command:

```bash
git add main.py select_habitat.py
```

Open the repository in your browser. 
Why the fines are not there?

## Commit the changes

You need to commit the changes to the repository.
To do this, you can use the following command:

```bash
git commit -m "Add main.py and select_habitat.py"
```

Open the repository in your browser. 
Why the fines are still not there?


## Push the changes

To push the changes to the remote repository, you can use the following command:

```bash
git push origin main
```

## Issues to consider

1. Why are the files not there after adding them?
2. Why are the files not there after committing them?
3. Why are the files there after pushing them?
4. What is the difference between `git add`, `git commit`, and `git push`?
5. What is the purpose of the `-m` flag in the `git commit` command?
6. What is the purpose of the `origin` keyword in the `git push` command?


## Implement a new feature

The `select_habitat.py` file contains a function that selects a habitat for an alien species.
However, it is not implemented yet. 

A good practice is to create a new branch for each feature you implement.


## Create a new branch

To create a new branch, you can use the following command:

```bash
git checkout -b select-habitat
```

Now we have a new branch named `select-habitat` parallel to the `main` branch.
To vew the branches, you can use the following command:

```bash
git branch
```

Modify the `select_habitat.py` to implement the `select_habitat` function.
Set the contents of the `select_habitat.py`  to [select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/select-habitat/select_habitat.py).

Commit the changes and push them to the remote repository 
```bash
git add README.md 
git commit -m "implement function"
git push
```