# Openshift Launchpad

A simple three-tiered application (database, server, client) that is designed to be run locally or depoyable to the BC Government OpenShift cluster with ease.

## Purpose

Most new project teams working within the BC Developers Exchange environment experience a lengthy acclimation period in which learn about the tools and environment of the lab. While familiar with developing apps, teams are often unaware of how to deploy them to OpenShift. OpenShift configuration and deployment itself is a steep learning curve. With all of the new things to learn and absorb, *Sprint Zero* can easily drag out for weeks.

This project is intended as a starting point for the team with a Product Owner who wants to start realizing business value as soon as possible after the project kicks off. This repository does not have everything necessary to solve every problem you will face, but it should work out of the box and allow you to add working features sooner.

## Philosophy

- Everything is open-source. 
- Keep things simple and add complexity when required.
- Automate repetitive commands while exposing what's being done.
- Obfuscate the underlying technology as little as possible.
- Able to clone, build, and run locally with minimal effort.
- Keep everything compatible with deployment to OpenShift.
- Minimize technical debt.

## Requirements:

- [Git](https://git-scm.com)
- [make](http://man7.org/linux/man-pages/man1/make.1.html) (installed by default on OS X and Linux)
- [Docker](https://www.docker.com/)
- [OpenShift CLI](https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html#cli-reference-get-started-cli)
- Docker Compose (included with [Docker](https://docs.docker.com/install/) on Windows and Mac; used to run locally)

## Getting Started

The application is fully containerized, simplifying both local development and deployment to OpenShift. The processes described in this document use Docker Compose to run services locally. Note that running the Python, Node, and PostgreSQL services locally without Docker containers is possible, but is left as an excersise for the reader. Further, note that the Docker Compose commands are not intended to interact in any way with OpenShift (see "Deployment" below).

### Local Deployment

1. Install [Docker](https://www.docker.com/) (if you haven't already)
2. Checkout the project `git clone https://github.com/bcgov/openshift-launchpad.git` (or use ssh)
3. Under the root directory, run `make run` in your terminal
4. Inspect the application services exposed at the following URLs.
	- The client container exposes port 3000 locally at http://localhost:3000
	- The server container exposes port 5000 locally at http://localhost:5000
	- The database container exposes port 5435 and can be inspected using pgAdmin, Postico, psql, etc.

### OpenShift Deployment

Before deploying to the BC Government OpenShift cluster, access must be granted. If you are a member of a new Developer Exchange team, you may have to request access. The BC Developer Exchange [provides a channel](https://github.com/BCDevOps/devops-requests) through which OpenShift access can be requested.

1. Ensure the [OpenShift CLI](https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html#cli-reference-get-started-cli) is installed `oc version`
2. Login to your OpenShift cluster using the CLI
	- Ensure you have access to the BC Gov OpenShift cluster (request access [here](https://github.com/BCDevOps/devops-requests/issues/new?template=openshift_user_access_request.md))
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

The project uses Make commands listed in the [Makefile](Makefile) for ease of development. The available commands are as follows.

| Command                 | Target    | Description
|-------------------------|-----------|----------------------------------------------------
| make build              | Local     | (Re-)Builds local images listed in the docker-compose
| make run                | Local     | Launches the application using Docker (builds the images if required)
| make restart            | Local     | Stops the app, rebuilds the images, and restarts the app
| make close              | Local     | Stops and removes any locally running containers
| make clean              | Local     | Purges containers, images, and volumes
| make client-test        | Local     | Runs client unit tests
| make create-nsp         | OpenShift | Creates the requisite Network Security Policies in OpenShift
| make create-database    | OpenShift | Creates the database service in OpenShift
| make create-server      | OpenShift | Creates the server service in OpenShift
| make create-client      | OpenShift | Creates the client servvice in OpenShift
| make oc-all-clean       | OpenShift | Removes all OpenShift objects associated with the application (does not affect persisted objects)
| make oc-database-clean  | OpenShift | Removes all OpenShift objects associated with the database service (does not affect persisted objects)
| make oc-persisted-clean | OpenShift | Removes all persisted objects associated with the application (NSPs, volume claims, and secrets)
| make oc-server-clean    | OpenShift | Removes all OpenShift objects associated with the server service
| make oc-client-clean    | OpenShift | Removes all OpenShift objects associated with the client service

Refer to the [Makefile](Makefile) for arguments required for the above commands.

## License

Code released under the [Apache License, Version 2.0](LICENSE).
