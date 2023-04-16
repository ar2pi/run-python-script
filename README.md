# run-python-script

- **Docker image:** [ar2pi/run-python-script](https://hub.docker.com/repository/docker/ar2pi/run-python-script)

## Requirements

- [Docker](https://www.docker.com/)

## Run containerized python script

```sh
# python 3
docker run -v $(pwd):/code ar2pi/run-python-script python script_file.py

# python 2
docker run -v $(pwd):/code ar2pi/run-python-script:python2 python script_file.py
```

## Debug within container

```sh
# python 3
docker run -it -v $(pwd):/code ar2pi/run-python-script /bin/bash

# python 2
docker run -it -v $(pwd):/code ar2pi/run-python-script:python2 /bin/bash
```

## Setup new project

```sh
export PROJECT_NAME=[YOUR_PROJECT_NAME]
git clone git@github.com:ar2pi/run-python-script.git $PROJECT_NAME
cd $PROJECT_NAME
docker build -t $PROJECT_NAME .

# run main.py
docker run -v $(pwd)/src:/code $PROJECT_NAME
# debug
docker run -it -v $(pwd)/src:/code $PROJECT_NAME /bin/bash
```

## Dev container

To get intellisense and all that jazz your editor needs to run in a container with python's runtime and libraries.

### Vscode

When opening the project folder you should see an option *"Reopen in Container"* ➜ click on that. Or open the command palette (CTRL + Shift + P) + search for *"Dev Containers: Reopen in Container"*.  

[.devcontainer.json](.devcontainer.json) contains the necessary configuration.

For reference see [vscode docs](https://code.visualstudio.com/docs/devcontainers/create-dev-container).
