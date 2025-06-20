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

## Login to GitHub from your device

To edit the remote repository from your device, you need to login to GitHub.
You have two options:

- **(recommended)** With the [GitHub CLI client](https://cli.github.com/) (`gh`)
  - Install `gh`, following the [instructions from their website](https://cli.github.com/)
  - In the terminal, run
    ```shell
    gh auth login
    ```
  - Follow the steps in the terminal (pick `GitHub.com`, `HTTPS` and `Login with a web browser` when asked)
  - Follow the steps in the browser
  - You can now clone repositories using `git clone https://github.com/USER-NAME/REPO-NAME` (see next section)
- (advanced) With SSH keys
  - Setup SSH authentication following the [GitHub documentation](https://docs.github.com/en/get-started/git-basics/about-remote-repositories#cloning-with-ssh-urls)
  - You can now clone repositories using `git clone git@github.com:USER-NAME/REPO-NAME.git`

## Add new files

Clone the repository to your local machine using the following command 
(make sure to replace `USER-NAME` with your GitHub username):

```bash
git clone https://github.com/USER-NAME/git-tutorial
```

Go to the folder where you cloned the repository

Open a file editor and create a new file named `app/main.py` and add the contents from 
[main.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/main/app/main.py) to it.

Also create a new file named `app/select_habitat.py` and add the contents from 
[select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/main/app/select_habitat.py) to it.

Now you can add the files to the repository using the following command:

```bash
git add app/
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

The `select_habitat.py` file contains a function that selects a habitat for an 
alien species.
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
Set the contents of the `select_habitat.py`  to [select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/select-habitat/app/select_habitat.py).

Commit the changes and push them to the remote repository 
```bash
git add app/select_habitat.py
git commit -m "implement function"
git push origin select-habitat
```

## Add new features in parallel 

If you are woking in a team you can assign the implementation of different features to different team members. 
To do this, you can create a new branch for each feature.

### Implement param_climate_model

To implement the `param_climate_model` function, create a new branch named `param_climate_model`:

```bash
git checkout -b param_climate_model
```
Now modify the `select_habitat.py` file to implement the `param_climate_model` function.
The file should look like this: [select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/param_climate_model/app/select_habitat.py).

Commit the changes and push them to the remote repository:

```bash
git add app/select_habitat.py
git commit -m "Implement param_climate_model"
git push origin param_climate_model
```


### Implement param_species_class

To implement the `param_species_class` function, create a new branch named `param_species_class`:

```bash
git checkout -b param_species_class
```
Now modify the `select_habitat.py` file to implement the `param_species_class` function.
The file should look like this: [select_habitat.py](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/param_species_class/app/select_habitat.py).


Commit the changes and push them to the remote repository:

```bash
git add app/select_habitat.py
git commit -m "Implement param_species_class"
git push origin param_species_class
```

## Merge branches

Now we have three branches: `main`, `select-habitat`, `param_climate_model`, and `param_species_class`.

To look at the branches, you can use the following command:

```bash
git branch
```
To merge the `select-habitat` branch into the `main` branch, you need to switch to the `main` branch first:

```bash
git checkout main
git fetch origin
```
Now you can merge the `select-habitat` branch into the `main` branch using the following command:

```bash
git merge select-habitat
```

If there are no conflicts, the merge will be successful.

We can now push the changes to the remote repository:

```bash
git push origin main
```

To merge the `param_climate_model` branch into the `main` branch we run

```bash
git merge param_climate_model
```

If there are no conflicts, the merge will be successful.


## Issues to consider

1. What is the purpose of creating a new branch for each feature?

# Docker 

To make sure that the code runs on any machine, we can use Docker to create a container with the code and its dependencies.

## Install Docker

### MacOS
To install Docker on MacOS, you can use https://docs.docker.com/desktop/install/mac-install/

### Windows
To install Docker on Windows, you can use https://docs.docker.com/desktop/install/windows-install/


## Create a Dockerfile

A Dockerfile is a file that contains instructions on how to build a Docker image including the dependencies and the code.
Like implementing the `select_habitat` function, we need to create a new branch for this task.


```bash
git checkout -b docker-setup
```

Create a new file named `Dockerfile` in the root of the repository and add the 
following contents to it [Dockerfile](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/docker-setup/Dockerfile)

Create a new file named `requirements.txt` in the root of the repository and add the
following contents to it [requirements.txt](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/docker-setup/requirements.txt)

Now we can build the Docker image using the following command:

```bash
docker build -t git-tutorial .
```

## CI/CD workflow

In this section, we will create a CI/CD workflow to automatically build the Docker image.

To create a CI/CD workflow with GitHub actions, we will create a YAML file in `.github/workflows/`, which contains the steps for the CI/CD workflow.

Start from the `docker-setup` branch and create a new branch:

```shell
git checkout -b cicd-workflow
```

Create a new file named `.github/workflow/ci-pipeline.yaml` and add the following contents to it: [ci-pipeline.yaml](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/cicd-workflow/.github/workflows/ci-pipeline.yaml).

Edit `.github/workflow/ci-pipeline.yaml` to replace `user-name` with your GitHub username (line 14).

Create a new file named `.github/workflow/build-docker.yaml` and add the following contents to it: [build-docker.yaml](https://raw.githubusercontent.com/QCDIS/git-tutorial/refs/heads/cicd-workflow/.github/workflows/build-docker.yaml)

Commit and push the changes:

```shell
git add .github
git commit -m "add CICD pipeline"
git push origin cicd-workflow
```

Check the actions tab in your GitHub repository. What is the workflow doing? Where are its outputs?

Create a release on your repository, and check the Actions tab. What is the workflow doing? Where are its outputs?
