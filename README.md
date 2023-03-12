# run-python-script

Boilerplate to run containerized python scripts.

## Requirements

- [Docker](https://www.docker.com/)

## Setup

```sh
# Replace [PROJECT_NAME] with your project name
git clone git@github.com:ar2pi/run-python-script.git [PROJECT_NAME]

docker build -t [PROJECT_NAME] .
```

## Run

```sh
docker run -v $(pwd)/src:/code [PROJECT_NAME]
```

## Debug

```sh
docker run -it -v $(pwd)/src:/code [PROJECT_NAME] /bin/bash
```

## Dev container

To get intellisense and all that jazz you need to point your editor to use a running container for python runtime.

### Vscode 

See -> https://code.visualstudio.com/docs/devcontainers/create-dev-container

[.devcontainer.json](.devcontainer.json) contains all necessary configuration. When opening the project folder you should see an option "Reopen in Container", click on that. Or open command palette (CTRL + Shift + P) and search for "Dev Containers: Reopen in Container".
