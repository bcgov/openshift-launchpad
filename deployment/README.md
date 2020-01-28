# CI/CD

This project uses the following technologies to facilitate the development and deployment process.

GitHub : Code repository to store and track changes.
Docker : To run application on any platform regardless of OS/Architecture differences.
Docker Compose : To manage and orchestrate container life cycle.
Jenkins : To orchestrate the CI/CD process of the different environments.

The files listed below are required for the process to run smoothly.

```
|-- client
    |-- Dockerfile (Docker image build definition for the nodejs client)

|-- database
    |-- Dockerfile (Docker image build definition for the postgres database)

|-- deployment
    |-- docker-compose.yml (Jenkins container orchestration config)
    |-- scripts (scripts to help facilitate deployment)
    |-- jenkins (Configuration files for the Jenkins application)

|-- server
    |-- Dockerfile (Docker image build definition for the python server)

|-- docker-compose.yml (Application containers orchestration to help with local development)
|-- docker-compose-ci.yml (Application containers orchestration to help with CI/CT on Jenkins)
|-- docker-compose-cd.yml (Application containers orchestration to help with CD on remote servers)
|-- Jenkinsfile (Pipeline definition to run on Jenkins)
```

## Jenkins

The application uses a containerized version of Jenkins to handle CI/CD part of the pipeline flow.
The flow defined in the Jenkinsfile is as follows:

Developer creates a Pull Request on Github. -> Github fires a webhook to Jenkins to start the CI flow -> Jenkins builds the application container images -> Runs unit tests on the application components -> Deploys the application to the remote instance using SSH (Only if the target branch of PR is master) -> Cleans up any build artifacts.

## Running Jenkins

Build the container image by executing `docker-compose build` at the root of the deployment directory.
The build process will fetch the base jenkins image, install docker, docker-compose and all the plugins from plugins.txt into it.

To launch the container, run the following command : `docker-compose up`

## Jenkins Configuration

The default login for jenkins is `admin:admin`. It is strongly recommended to change the password after first login.

The following configuration needs to be done manually for the flow to work end to end properly:

- Add a Github Webhook for the [MultiBranch Scan Plugin](https://wiki.jenkins.io/display/JENKINS/Multibranch+Scan+Webhook+Trigger+Plugin).

- Add your Github credentials to the MultiBranchPlugin pipeline configuration if you're trying to access a private repository.

- Add the following environment variable to the jenkins global environment to be injected into the job build.

```
AWS_INSTANCE_IP_ADDRESS : IP address of the cloud instance you want to deploy the application on. (The instance must have docker and docker-compose installed).

```

- Add a secrets file to jenkins Credentials with the id `swu-prod-env` and replace values inside `<>` with production credentials.

```
export POSTGRES_USER=<POSTGRES_USER>
export POSTGRES_PASSWORD=<POSTGRES_PASSWORD>

export SMTP_USERNAME=<SMTP_USERNAME>
export SMTP_PASSWORD=<SMTP_PASSWORD>

```

- Add the SSH key to Jenkins Credentials required to login into the remote instance with the id `ssh-instance-key`.

## Github Flow

The application uses [Github Flow](https://guides.github.com/introduction/flow/) for the CI/CD process.

- Feature branches open a PR against the dev branch, and go through the CI flow.

- A PR is created from dev targeting master branch, that runs through the CI/CD flow.
