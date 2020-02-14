# Openshift Launchpad

This codebase is contains a very simple project that has been minimized as much as possible and is designed to be depoyable in BC Gov OpenShift

## Purpose

Most new project teams working within the BC Developers Exchange environment experience a kick-off period where they need to learn the tools and processes necessary to create and deploy a new application. Even something as seemingly simple as implementing a reference 3-tiered architecture can occupy a great deal of development time if the team doesn't start with a simple boilerplate. OpenShift configuration and deployment itself is a steep learning curve. With all of the new things to learn and absorb, "Sprint Zero" can easily drag out for weeks.

This project is intended as a starting point for the team with a Product Owner who wants to start realizing business value soon after the project kicks off. The repo before you does not have everything necessary to solve every problem you will face, but it should work out of the box and allow you to put working features in front of users sooner. 

## Philosophy
- Everything is Open-Source. 
- Keep things as simple as possible (you can make it more complicated later if you need to).
- Automate as much as possible (you can find all the scripts and run them manually if you want to).
- We should be able to check out, build and run locally with minimal effort (using docker-compose).
- Keep everything compatible with deployment to OpenShift.
- Reduce technical debt as much as possible and keep cleaning it up as you go.

## Requirements:
- Git
- “Make” (installed by default on OS X and Linux)
- [Docker](https://www.docker.com/)
- OpenShift CLI
- Docker Compose (included with Docker on Windows and Mac; only for convenience when running locally)

## Getting Started
The application is fully Dockerized, which makes deployment to OpenShift possible. An additional benefit is that the application can easily be run locally as a Docker network using Docker-Compose. If someone prefers to run Python, Node and PostgreSQL directly on their workstation as individual services that is fully possible, but the seamless experience described here lends itself to easy setup and switching between branches. Not that the Docker-Compose commands are not intended to interact in any way with OpenShift (see "Deployment" below).

1. Install [Docker](https://www.docker.com/) (if you haven't already)
1. Checkout the code: git clone https://github.com/bcgov/openshift-launchpad.git (or use ssh)
1. Under the root directory, run `make run` in your terminal
1. Visit the application on the following ports/URLs:
	- The client container exposes port 3000 and can be viewed by visiting http://localhost:3000
	- The server container exposes port 5000 and can be viewed by visiting http://localhost:5000
	- The database container exposes port 5435 and can be viewed by using pgAdmin, postico, or psql

## Deployment

Write-up TODO

## Commands

The project uses Make commands listed in the [Makefile](Makefile) for ease of development. The commands are as follows:

| Command         | Description                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------|
| make build      | (Re-)Builds container images listed in the docker-compose                                   |
| make run        | Launches the application using Docker (Builds the images if they haven't been built before) |
| make close      | Stops and removes any running containers                                                    |
| make restart    | Stops the app, rebuilds the images and restarts the app                                     |
| make clean      | Purges containers, images and volumes                                                       |
| make db-upgrade | Run database migrations                                                                     |
| make pylint     | Runs the linter on the Python code base and reports errors.  This command requires a few more things set up in your local environment (see the Makefile for details).


## License

Code released under the [Apache License, Version 2.0](LICENSE).
