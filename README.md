# Openshift Launchpad

This codebase is a wrapper for creating applications that will run on [Openshift](https://www.openshift.com/). 
Deployment logic has been pre-configured for your convenience.

Estimated time to deploy the app:
- Locally: ~2-5 min
- Openshift: ~30 min

Created by: [FreshWorks Studio](https://freshworks.io)

#### Requirements:

- [Docker](https://www.docker.com/)

## Getting Started

1. Install [Docker](https://www.docker.com/) (if you haven't already)

2. Under the root directory, run `make run` in your terminal

3. Visit the application on the following ports/URLs:
    - The client container exposes port 3000 and can be viewed by visiting http://localhost:3000
    - The server container exposes port 5000 and can be viewed by visiting http://localhost:5000
    - The database container exposes port 5432 and can be viewed by using pgAdmin.

## Commands

The project uses Make commands listed in the [Makefile](Makefile) for ease of development. The commands are as follows:

| Command         | Description                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------|
| make build      | (Re-)Builds container images listed in the docker-compose                                   |
| make run        | Launches the application using Docker (Builds the images if they haven't been built before) |
| make stop       | Stops and removes any running containers                                                    |
| make restart    | Stops the app, rebuilds the images and restarts the app                                     |
| make clean      | Purges containers, images and volumes                                                       |
| make db-upgrade | Run database migrations                                                                     |

## Deployment

Write-up TODO

## License

Code released under the [Apache License, Version 2.0](LICENSE).
