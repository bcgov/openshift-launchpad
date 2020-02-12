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

stop:
	@echo "+\n++ Stopping client and server ...\n+"
	@docker-compose down

clean:
	@echo "+\n++ Removing containers, images, volumes etc ..."
	@echo "+\n++ Note: does not clear image cache \n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f openshift-launchpad_postgres-data

##############################################################################
# Deployment commands
##############################################################################

############################
# Generic commands
############################

oc-all-clean:
	@echo "+\n++ Tearing down all OpenShift objects created from templates...\n+"
	@oc delete all -l app=openshift-launchpad

server:
	oc-server-build NAMESPACE=$(NAMESPACE)
	oc-server-deploy NAMESPACE=$(NAMESPACE) POSTGRESQL_USER=$(POSTGRESQL_USER) POSTGRESQL_PASSWORD=$(POSTGRESQL_PASSWORD)

database:
	oc-db-build NAMESPACE=$(NAMESPACE)
	oc-db-deploy DATABASE_SERVICE_NAME=$(DATABASE_SERVICE_NAME) POSTGRESQL_USER=$(POSTGRESQL_USER) POSTGRESQL_PASSWORD=$(POSTGRESQL_PASSWORD) POSTGRESQL_DATABASE=${POSTGRESQL_DATABASE}

client:
	oc-client-build NAMESPACE=$(NAMESPACE)
	oc-client-deploy NAMESPACE=$(NAMESPACE)

############################
# Server commands
############################

oc-server-build:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=mynamespace
	@echo "+\n++ Creating OpenShift server build config and image stream...\n+"
	@oc process -f deployment/server.bc.json -p NAMESPACE=$(NAMESPACE) | oc create -f -

oc-server-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(POSTGRESQL_USER)" # Please provide a database user via POSTGRESQL_USER=admin
	test -n "$(POSTGRESQL_PASSWORD)" # Please provide a database password via POSTGRESQL_PASSWORD=password
	@echo "+\n++ Creating OpenShift server deployment config, services, and routes...\n+"
	@oc process -f deployment/server.dc.json -p NAMESPACE=$(NAMESPACE) POSTGRESQL_USER=$(POSTGRESQL_USER) POSTGRESQL_PASSWORD=$(POSTGRESQL_PASSWORD) | oc create -f -

oc-server-clean:
	@echo "+\n++ Tearing down OpenShift server objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-server

############################
# Database commands
############################

oc-db-build:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	@echo "+\n++ Creating OpenShift database build config and image stream...\n+"
	@oc process -f deployment/db.bc.json -p NAMESPACE=$(NAMESPACE) | oc create -f -

oc-db-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(DATABASE_SERVICE_NAME)" # Please provide a database service name via DATABASE_SERVICE_NAME=db-service
	test -n "$(POSTGRESQL_USER)" # Please provide a database user via POSTGRESQL_USER=admin
	test -n "$(POSTGRESQL_PASSWORD)" # Please provide a database password via POSTGRESQL_PASSWORD=password
	test -n "$(POSTGRESQL_DATABASE)" # Please provide a database name via POSTGRESQL_DATABASE=sample_db
	@echo "+\n++ Creating OpenShift database deployment config, services, and routes...\n+"
	@oc process -f deployment/db.dc.json -p NAMESPACE=$(NAMESPACE) DATABASE_SERVICE_NAME=$(DATABASE_SERVICE_NAME) POSTGRESQL_DATABASE=$(POSTGRESQL_DATABASE) POSTGRESQL_USER=$(POSTGRESQL_USER) POSTGRESQL_PASSWORD=$(POSTGRESQL_PASSWORD) | oc create -f -

oc-db-clean:
	@echo "+\n++ Tearing down OpenShift postgresql objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-database

oc-db-storage-rm:
	test -n "$(DATABASE_SERVICE_NAME) # Please provide a database service name via DATABASE_SERVICE_NAME=db-service
	@echo "+\n++ Remove persistant storage used by db service \n+"
	@oc volume pvc/$(DATABASE_SERVICE_NAME) --remove

############################
# Client commands
############################

oc-client-build:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	@echo "+\n++ Creating OpenShift client build config and image stream...\n+"
	@oc process -f deployment/client.bc.json -p NAMESPACE=$(NAMESPACE) | oc create -f -

oc-client-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	@echo "+\n++ Creating OpenShift client deployment config, services, and routes...\n+"
	@oc process -f deployment/client.dc.json -p NAMESPACE=$(NAMESPACE) | oc create -f -

oc-client-clean:
	@echo "+\n++ Tearing down OpenShift client objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad-client
