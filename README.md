# IU DevOps Lab 1

## CI

![app python badge](https://github.com/behouba/devOpsLab/actions/workflows/ci.yml/badge.svg)

##  Requirements
- Python 3.9+
- pip 22+
- Flask 2.1.2

## Flask

Flask is an open-source micro framework for web development in Python. It is classified as microframework because it is very lightweight. Flask aims to keep the core simple but extensible.
Flask is robust, solid, adaptable, scalable and user-friendly web framework. 

Flask's built-in server is not production ready according the the Official documentation.


>While lightweight and easy to use, Flask’s built-in server is not suitable for production as it doesn’t scale well. Some of the options available for properly running Flask in production are documented  [here](https://flask.palletsprojects.com/en/2.1.x/deploying/).



To be deployed in production they are several options available from the [official documentation](https://flask.palletsprojects.com/en/2.1.x/deploying/) of Flask.



## Installation

Clone the repository

```bash
git clone https://github.com/behouba/devOpsLab

cd devOpsLab/app_python
```

Create and activate a virtual environement

```bash
python3 -m venv env


virtualenv venv


. ./venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the app

```bash
python3 main.py
```


## Run tests

```bash
pytest .
```

## Docker

Build the docker image locally

```bash
sudo docker build -t lab2 .
```

Scan the docker image to check for vunerabilities:

```bash
sudo docker scan lab2
```

Start a new container

```bash
docker run -d -p 5000:5000
```

The docker image is also available on DockerHub.

```bash
docker pull behouba/devops-labs:lab2

docker run -d -p 5000:5000 behouba/devops-labs:lab2
```

## Unit tests

Run the unit tests with the following command:

```bash
$ python3 -m unittest -v 
```