# Python web application

## Overview

This web application provides the current time in the Moscow time zone.

## Running application

1. Ensure you have `Python 3` installed by running:

   ```properties
   python --version
   ```

   or

   ```properties
   python3 --vresion
   ```

   Verify that the version is greater than or equal to 3.0.0.

2. Navigate to app_python.

3. Create and activate virtual evnironment.

4. Install requirements

   ```properties
   pip install -r requirements.txt
   ```

5. Start the application using:

   ```properties
   flask --app app run
   ```

6. Go to the link shown in the terminal, and you will get the time in Moscow.

## Unit tests

For testing purposes, you can execute all tests by running the following command inside the `/app_python` directory:

```properties
pytest
```

## Docker

### Pull

Run the following command to pull docker image from docker hub

```properties
docker pull ahmadalhussin/app_python:latest
```

### Build

Run the following command to build docker image

```properties
docker build --tag ahmadalhussin/app_python .
```

### Run 

To start the image

```properties
docker run -d -p 5000:5000 ahmadalhussin/app_python
```

## CI

For Continuous Integration I created multiple yml files in `.github/workflows/` directory.

For each one, multiple parts are being runned to achieve the desired goal.

The first part is to build the application. This stage consist of the following:

- Install dependencies

- Running unit tests

- Linting/building project

The second part is to do security check with snyk

The final part is to push our docker image to docker hub. This part is divided also to:

- Login to docker hub using GitHub secrect

- Build Image

- Tag the Image

- Push the image to docker hub
