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
