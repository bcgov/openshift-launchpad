#!make

##############################################################################
# Development commands
##############################################################################

restart: stop build run

build:
	@echo "+\n++ Building images ...\n+"
	@docker-compose build

run:
	@echo "+\n++ Running client and server ...\n+"
	@docker-compose up -d

run-server:
	@echo "+\n++ Running server ...\n+"
	@docker-compose up -d server

stop:
	@echo "+\n++ Stopping client and server ...\n+"
	@docker-compose down

db-seed:
	@echo "+\n++ Seeding database ...\n+"
	@docker-compose run server python manage.py seed-db

clean:
	@echo "+\n++ Removing containers, images, volumes etc..."
	@echo "+\n++ Note: does not clear image cache \n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f openshift-launchpad_postgres-data

##############################################################################
# Deployment commands
##############################################################################

## Generic commands

oc-all-clean:
	@echo "+\n++ Tearing down all OpenShift objects created from templates...\n+"
	@oc delete all -l app=openshift-launchpad

## Server commands

oc-server-build:
	@echo "+\n++ Creating OpenShift build config and image stream...\n+"
	@oc process -f deployment/server.bc.json | oc create --validate -f -

oc-server-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=mynamespace
	@echo "+\n++ Creating OpenShift deployment config, services, and routes...\n+"
	@oc process -f deployment/server.dc.json -p NAMESPACE=$(NAMESPACE) | oc create --validate -f -

oc-server-clean:
	@echo "+\n++ Tearing down OpenShift server objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-server

## Database commands

oc-db-build:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	@echo "+\n++ Creating OpenShift DB build config and image stream...\n+"
	@oc process -f deployment/db.bc.json -p NAMESPACE=$(NAMESPACE) | oc create --validate -f -

oc-db-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(DATABASE_SERVICE_NAME)" # Please provide a namespace via DATABASE_SERVICE_NAME=db-service
	test -n "$(POSTGRESQL_USER)" # Please provide a namespace via POSTGRESQL_USER=admin
	test -n "$(POSTGRESQL_PASSWORD)" # Please provide a namespace via POSTGRESQL_PASSWORD=password
	test -n "$(POSTGRESQL_DATABASE)" # Please provide a namespace via POSTGRESQL_DATABASE=sample_db
	@echo "+\n++ Creating OpenShift deployment config, services, and routes...\n+"
	@oc process -f deployment/db.dc.json -p NAMESPACE=$(NAMESPACE) DATABASE_SERVICE_NAME=$(DATABASE_SERVICE_NAME) POSTGRESQL_DATABASE=$(POSTGRESQL_DATABASE) POSTGRESQL_USER=$(POSTGRESQL_USER) POSTGRESQL_PASSWORD=$(POSTGRESQL_PASSWORD) | oc create --validate -f -

oc-db-clean:
	@echo "+\n++ Tearing down OpenShift postgresql objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-database

oc-db-storage-rm:
	test -n "$(DATABASE_SERVICE_NAME) # database service name
	@echo "+\n++ Remove persistant storage used by db service \n+"
	@oc volume pvc/$(DATABASE_SERVICE_NAME) --remove

## Client commands

oc-client-build:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(REPO_URL)" # Please provide a repository url via REPO_URL=https://github.com/bcgov/my-repo-name
	test -n "$(BRANCH_NAME)" # Please provide a branch name via BRANCH_NAME=origin/dev
	@echo "+\n++ Creating OpenShift DB build config and image stream...\n+"
	@oc process -f deployment/client.bc.json -p NAMESPACE=$(NAMESPACE) REPO_URL=$(REPO_URL) BRANCH_NAME=$(BRANCH_NAME) | oc create --validate -f -

oc-client-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	@echo "+\n++ Creating OpenShift deployment config, services, and routes...\n+"
	@oc process -f deployment/client.dc.json -p NAMESPACE=$(NAMESPACE) | oc create --validate -f -

oc-client-clean:
	@echo "+\n++ Tearing down OpenShift client objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-client
