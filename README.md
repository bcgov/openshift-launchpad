# Openshift Launchpad

A simple three-tiered application (database, server, client) that is designed to be run locally or depoyable to the BC Government OpenShift cluster with ease.

## Purpose

Most new project teams working within the BC Developers Exchange environment experience a kick-off period where they need to learn the tools and processes necessary to create and deploy a new application. Even something as seemingly simple as implementing a reference 3-tiered architecture can occupy a great deal of development time if the team doesn't start with a simple boilerplate. OpenShift configuration and deployment itself is a steep learning curve. With all of the new things to learn and absorb, "Sprint Zero" can easily drag out for weeks.

This project is intended as a starting point for the team with a Product Owner who wants to start realizing business value soon after the project kicks off. The repo before you does not have everything necessary to solve every problem you will face, but it should work out of the box and allow you to put working features in front of users sooner. 

## Philosophy
- Everything is Open-Source. 
- Keep things as simple as possible (you can make it more complicated later if you need to).
- Automate as much as possible (you can find all the scripts and run them manually if you want to).
- Obfuscate the underlying technology as little as possible.
- We should be able to check out, build and run locally with minimal effort (using docker-compose).
- Keep everything compatible with deployment to OpenShift.
- Reduce technical debt as much as possible and keep cleaning it up as you go.

## Requirements:
- [Git](https://git-scm.com)
- [make](http://man7.org/linux/man-pages/man1/make.1.html) (installed by default on OS X and Linux)
- [Docker](https://www.docker.com/)
- [OpenShift CLI](https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html#cli-reference-get-started-cli)
- Docker Compose (included with [Docker](https://docs.docker.com/install/) on Windows and Mac; only for convenience when running locally)

## Getting Started
The application is fully Dockerized, simplifying both local development and deployment to OpenShift. If someone prefers to run Python, Node, and PostgreSQL directly on their workstation as individual services that is fully possible, but the seamless experience described here lends itself to easy setup and switching between branches. Note that the Docker-Compose commands are not intended to interact in any way with OpenShift (see "Deployment" below).

### Local Deployment

1. Install [Docker](https://www.docker.com/) (if you haven't already)
2. Checkout the code `git clone https://github.com/bcgov/openshift-launchpad.git` (or use ssh)
3. Under the root directory, run `make run` in your terminal
4. Visit the application on the following ports/URLs:
	- The client container exposes port 3000 and can be viewed by visiting http://localhost:3000
	- The server container exposes port 5000 and can be viewed by visiting http://localhost:5000
	- The database container exposes port 5435 and can be viewed by using pgAdmin, postico, psql, etc.

### OpenShift Deployment

1. Ensure the OpenShift CLI is installed `oc version`
2. Login to your OpenShift cluster using the CLI
	- Login to the BC Gov OpenShift cluster [here](https://console.pathfinder.gov.bc.ca:8443/console/)
	- Ensure there is at least one namespace that you have rights to edit
	- Click your name in the top right to reveal a dropdown
	- Click "Copy Login Command"
	- Paste into your terminal
3. From the root project directory, run `make create-nsp NAMESPACE=[NAMESPACE] APP_NAME=[APP_NAME]` replacing `[NAMESPACE]` with the ID of your OpenShift namespace and `[APP_NAME]` with an arbitrary application name (as per Kubernetes [requirements](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names), must meet [RFC-1123](https://tools.ietf.org/html/rfc1123))
4. Run `make create-database NAMESPACE=[NAMESPACE] APP_NAME=[APP_NAME] POSTGRESQL_DATABASE=[POSTGRESQL_DATABASE]` replacing `[POSTGRESQL_DATABASE]` with an arbitrary database name
5. Using the clsuter console, wait for the database to become fully deployed i.e. scale to one or more pods
6. Run `make create-server NAMESPACE=[NAMESPACE] APP_NAME=[APP_NAME] REPO=https://github.com/bcgov/openshift-launchpad BRANCH=develop`
7. Once the server has deployed, note the route that it exposes
	- Using the OpenShift console, navigate to Applications > Routes
	- The relevant route will be named [APP_NAME]-server
	- Copy the URL that the route exposes
7. Run `make create-client NAMESPACE=[NAMESPACE] APP_NAME=[APP_NAME] REPO=https://github.com/bcgov/openshift-launchpad BRANCH=develop API_URL=[API_URL]` replacing `[API_URL]` with the route URL copied in the previous step
8. Once the client is built and deployed, confirm it's working by navigating to the route it exposes

## Commands

The project uses Make commands listed in the [Makefile](Makefile) for ease of development. The commands are as follows:

| Command                 | Description
|-------------------------|---------------------------------------------------------------
| make build              | (Re-)Builds local images listed in the docker-compose
| make run                | Launches the application using Docker (builds the images if required)
| make restart            | Stops the app, rebuilds the images, and restarts the app
| make close              | Stops and removes any locally running containers
| make clean              | Purges containers, images, and volumes
| make client-test        | Runs client unit tests
| make create-nsp         | Creates the requisite Network Security Policies in OpenShift
| make create-database    | Creates the database service in OpenShift
| make create-server      | Creates the server service in OpenShift
| make create-client      | Creates the client servvice in OpenShift
| make oc-all-clean       | Removes all OpenShift objects associated with the application (does not affect persisted objects)
| make oc-database-clean  | Removes all OpenShift objects associated with the database service (does not affect persisted objects)
| make oc-persisted-clean | Removes all persisted objects associated with the application (NSPs, volume claims, and secrets)
| make oc-server-clean    | Removes all OpenShift objects associated with the server service
| make oc-client-clean    | Removes all OpenShift objects associated with the client service

Refer to the [Makefile](Makefile) for arguments required for the above commands.

## License

Code released under the [Apache License, Version 2.0](LICENSE).
