# Time Table Web App

Simple web application written in go which shows the time in Moscow on each page reload.

## Prerequisites

Before launching application install `requirements.txt` using `pip`:

```bash
    pip install -r requirements.txt

```

## Starting the app

To start the server, run from `app_python` folder:

```bash
    uvicorn --host <HOST> --port <PORT> server:server
```

Afterwards, this application will be available on `<host>:<port>/`

## Docker

This application can be containerized with docker.

### Build or Pull

You can build a container by running:

```bash
docker build -t <TAG> app_python/
```

Or you can pull existing container from Docker Hub:

```bash
docker pull ramprin/devops_py:latest
```

### Run

In order to run container use the following command:

```bash
docker run -p 80:8080 ramprin/devops_py:latest
```

After this, your application will be available on <http://localhost>
