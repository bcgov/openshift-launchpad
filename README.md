# Minimal React + Python Boilerplate

## Installation and Usage

This file describes how to run the project and develop against it.
NOTE: The instructions below haven't been tested on windows. If you are using windows
it is recommended to use WSL (Windows Subsytem for Linux).

### Starting a New Project

This repo uses [git
submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). If you will
be using this repo as a starting-point for a new project, it is recommended
that you use the following command to setup the repo once you have cloned it.

This will:
- Install the client submodule
- Remove unnecessary files
- Reinitialize the git history


```
$ make setup
```

**NOTE:** Do not run this command if you would like to contribute to the
boilerplate. See the Contributing section for more details.

## Requirements

- Docker

## Getting Started

The project uses Make commands listed in the [Makefile](Makefile) for ease of development.

Please refer to [Makefile](Makefile) for a list of all commands. Some of the most common ones are listed as follows:

`make run` : Launches the application using docker (Builds the images if they haven't been built before)

`make run-server` : Launches the server using docker (Builds the images if they haven't been built before)

`make stop` : Stops any running containers

`make build` : (Re-)Builds container images listed in the docker-compose.

`make clean` : Purges containers, images and volumes.

`make restart` : Stops the app, rebuilds the images and restarts the app.

`make server-test` : Runs the server unit tests.

`make client-test` : Runs the client unit tests.

NOTE: If you're having any unexpected issues, it's best to run `make rebuild` to cleanup and rebuild containers from scratch.

## Container Information

- The client container exposes port 3000 and can be viewed by visiting http://localhost:3000
- The server container exposes port 5000 and can be viewed by visiting http://localhost:5000
- The database container exposes port 5432 and can be viewed by using pgAdmin.

## CI/CD

- The application uses Github Workflows to run CI/CD pipelines. For more information checkout the [Github Actions Readme](.github/workflows/README.md)

## Contributing

If you intended to make changes to this boilerplate, you will want to use one
of the following workflows.

### Backend/Deployment Changes

If you would like to update any of the Python and/or deployment code, you can
treat this repo like any other. Simply clone the repo, make a branch for your
changes, and open a PR for review against the `master` branch.

## License

Code released under the [Apache License, Version 2.0](LICENSE).
