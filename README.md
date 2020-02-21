# Openshift Launchpad

A simple three-tiered application (database, server, client) that is designed to be run locally or depoyable to the BC Government OpenShift cluster with ease.

## Purpose

Most new project teams working within the BC Developers Exchange environment experience a lengthy acclimation period in which they learn about the tools and environment of the lab. While familiar with developing apps, teams are often unaware of how to deploy them to OpenShift. The concept of OpenShift configuration and deployment itself has a steep learning curve. With all of the new things to learn and absorb, *Sprint Zero* can easily drag out for weeks.

This project is intended as a starting point for the team with a Product Owner who wants to start realizing business value as soon as possible after the project kicks off. This repository does not have everything necessary to solve every problem you will face, but it should work out of the box and allow you to add features sooner.

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

1. Install [Docker](https://www.docker.com/)
2. Checkout the project `git clone https://github.com/bcgov/openshift-launchpad.git`
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
	- Ensure there is at least one namespace that you have rights to edit and note its ID
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

## Minishift Deployment

Minishift is a tool that helps run OpenShift locally. A single-node cluster is created inside a VM. Minishift can be installed using [these instructions](https://docs.okd.io/latest/minishift/getting-started/installing.html#installing-with-homebrew).

After installing, you'll have to run `minishift start` to spin up the cluster. Similar to the OpenShift console, Minishift provides a console that can be accessed from a web browser by running `minishift console`. Refer to the local Minishift console instead of the OpenShift console when following the steps outlined in the OpenShift Deployment section of this document.

## Deploying on Windows

We can run make commands in Windows using the following steps.
- Install [GNUWin](http://gnuwin32.sourceforge.net/)
- Find the installation location of GNUWin and its bin folder (eg: C:\\Program Files (x86)\\GnuWin32\\bin)
- Open the Environment Variables sections of Windows System Properties (see [instructions](https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0))
- Edit the `Path` environment variable and add the GNUWin bin directory from above (note that paths are comma separated)
- Reopen PowerShell or CMD and run make commands

## Database Migrations

The server portion of this project interacts with a PostgreSQL image. In order for the database to be created and configured, the server runs database migrations after deploying. Under the hood, this procedure relies on SQLAlchemy as an ORM. If changes are made to the applications model, this must be reflected in the migrations.

When you make changes to the model or add new model, run `flask db migrate -m "[YOUR MIGRATION COMMENTS]"`. Note that this command has the same dependencies as running the server itself. It can, therefore, be run inside the server Docker container or after installing the servers Python dependencies using `pip install -r server/requirements.txt` from the project root directory.

While migrations are run automatically when running the application locally using Docker Compose as well as when deploying to OpenShift, it is possible to run them directly. To update the database run `flask db upgrade`. Similarly, changes can be rolled back using `flask db downgrade`.

Docker Compose can be instructed to run only the migrations container by running `docker-compose start server-migrate`. Ensure the database container is already running as the migrations need a database on which to be applied.

## License

Code released under the [Apache License, Version 2.0](LICENSE).
