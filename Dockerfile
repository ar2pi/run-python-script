FROM python:3-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install additional deb packages
RUN apt-get update -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false && apt-get install -y \
    gcc \
    git \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# creates a non-root user and adds permission to access the /code folder
RUN groupadd -g 1000 slytherin \
    && useradd -u 1000 -g 1000 -s /bin/bash --create-home slytherin \
    && chown -R 1000:1000 /code
USER slytherin:slytherin

ENV PATH="/home/slytherin/.local/bin:${PATH}"

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./main.py" ]
