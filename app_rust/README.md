# LEARNING APPLICATION
![CI Rust](https://github.com/Ejedavy/S24-core-course-labs/actions/workflows/ci_rust.yaml/badge.svg)



This is a learning app that helps students learn school materials using AI.

<!-- Badges -->


![LEARNING APPLICATION](https://www.managedoutsource.com/wp-content/uploads/2023/06/artificial-intelligence-is-transforming-the-education-industry.jpg)

## Description

This has features that enables students create subjects and upload materials and use these materials to prepare for exams and study.

### Features

- Creating Subjects
- Uploading materials to train your personal study assistant
- Authentication

## Getting Started

### Installing

Clone the repository and build the project:

```bash
# Clone the repository
git clone https://github.com/Ejedavy/S24-core-course-labs.git

# Navigate to the project directory
cd S24-core-course-labs && cd app_learning


# Build the project
cargo build
```

## Executing program

Run the requirements for the application with:
```bash
bash ./script/init_db.sh

docker compose up
```

Run the program with:

```bash
cargo run
```

[![Local Host Application](https://i.postimg.cc/3N7xYPhg/image.png)](https://postimg.cc/k61myYB4)

Run tests with:

```bash
cargo test
```


### Docker

This repository contains a Dockerfile which you can build the image from or you could pull the image from docker hub.

To build the image, use the following command:

```bash
docker build -t app_rust .
```

To pull the image from the Docker Hub, use the following command:

```bash
docker pull ejedavid/app_rust:latest
```

After building or pulling the image, the container can be run with the following command:


```bash
docker run -p 8000:8000 app_run
```

The application will be available at [localhost:8000](http://localhost:8000/)


## Contributing

Contributions to this service are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.


## CI
A CI workflow is contained in the `.github/workflows/ci_rust.yaml` file. This workflow lints and tests the application, checks code vulnerability using SNYK, and builds and pushes docker image. Workflow is triggered only if the there is a change in the `app_rust` directory or the workflow file itself.

The CI workflow contains 3 jobs. Each job has a specific set of tasks to perform:

- test: This runs the unit tests of the application
- clippy: This is used for linting in the rust application.
- fmt: This is used for formatting the source code
- coverage: Checks code coverage


## Authors

- David Eje(https://github.com/ejedavy)
