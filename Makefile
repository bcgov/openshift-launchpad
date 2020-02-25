#!make

##############################################################################
# Development commands
##############################################################################

restart: close build run

run:
	@echo "+\n++ Running client and server...\n+"
	@docker-compose up -d

close:
	@echo "+\n++ Stopping client and server...\n+"
	@docker-compose down

build:
	@echo "+\n++ Building images...\n+"
	@docker-compose build

clean:
	@echo "+\n++ Removing containers, images, volumes etc...\n+"
	@echo "+\n++ Note: does not clear image cache. \n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f openshift-launchpad_postgres-data

client-test:
	@echo "+\n++ Running client unit tests...\n+"
	@docker-compose run client npm test

server-test:
	@echo "+\n++ Running server unit tests...\n+"
	@docker-compose run server python manage.py test

##############################################################################
# Deployment / CI-CD commands
##############################################################################

create-nsp:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	@echo "+\n++ Set network security policies \n+"
	@oc process -f deployment/nsp.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) | oc apply -f -

create-database:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	test -n "$(POSTGRESQL_DATABASE)" # Please provide a database name via POSTGRESQL_DATABASE=sample_db
	@echo "+\n++ Creating OpenShift database build config and image stream...\n+"
	@oc process -f deployment/database.bc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) | oc apply -f -
	@echo "+\n++ Creating OpenShift database deployment config, services, and routes...\n+"
	@oc process -f deployment/database.dc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) POSTGRESQL_DATABASE=$(POSTGRESQL_DATABASE) | oc apply -f -
	@echo "+\n++ Checking status of deployment.. \n+"
	@oc rollout status dc/${APP_NAME}-database

create-server:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	test -n "$(REPO)" # Please provide a git repo via REPO=https://github.com/bcgov/openshift-launchpad
	test -n "$(BRANCH)" # Please provide a git branch via BRANCH=develop
	@echo "+\n++ Creating OpenShift server build config and image stream...\n+"
	@oc process -f deployment/server.bc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) REPO=$(REPO) BRANCH=$(BRANCH) | oc apply -f -
	@echo "+\n++ Creating OpenShift server deployment config, services, and routes...\n+"
	@oc process -f deployment/server.dc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) | oc apply -f -
	@echo "+\n++ Checking status of deployment.. \n+"
	@oc rollout status dc/${APP_NAME}-server

create-client:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	test -n "$(REPO)" # Please provide a git repo via REPO=https://github.com/bcgov/openshift-launchpad
	test -n "$(BRANCH)" # Please provide a git branch via BRANCH=develop
	test -n "$(API_URL)" # Please provide a base API URL via API_URL=myproject
	@echo "+\n++ Creating OpenShift client build config and image stream...\n+"
	@oc process -f deployment/client.bc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) REPO=$(REPO) BRANCH=$(BRANCH) API_URL=$(API_URL) | oc apply -f -
	@echo "+\n++ Creating OpenShift client deployment config, services, and routes...\n+"
	@oc process -f deployment/client.dc.json -p NAMESPACE=$(NAMESPACE) APP_NAME=$(APP_NAME) | oc apply -f -
	@echo "+\n++ Checking status of deployment.. \n+"
	@oc rollout status dc/${APP_NAME}-client

##############################################################################
# Deployment cleanup commands
##############################################################################

oc-all-clean:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	@echo "+\n++ Tearing down all OpenShift objects created from templates...\n+"
	@oc project $(NAMESPACE)
	@oc delete all -l app=$(APP_NAME)
	@oc delete secret $(APP_NAME)-database --ignore-not-found

oc-database-clean:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	@echo "+\n++ Tearing down OpenShift postgresql objects created from templates...\n+"
	@oc project $(NAMESPACE)
	@oc delete all -l template=$(APP_NAME)-database
	@oc delete secret $(APP_NAME)-database --ignore-not-found

oc-persisted-clean:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide a database service name via DATABASE_SERVICE_NAME=db-service
	@echo "+\n++ Remove persistant storage used by db service \n+"
	@oc project $(NAMESPACE)
	@oc delete pvc $(APP_NAME)-database --ignore-not-found
	@oc delete secret $(APP_NAME)-database --ignore-not-found
	@oc delete nsp -l app=$(APP_NAME)

oc-server-clean:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	@echo "+\n++ Tearing down OpenShift server objects created from templates...\n+"
	@oc project $(NAMESPACE)
	@oc delete all -l template=$(APP_NAME)-server

oc-client-clean:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=myproject
	test -n "$(APP_NAME)" # Please provide an app name via APP_NAME=openshift-launchpad
	@echo "+\n++ Tearing down OpenShift client objects created from templates...\n+"
	@oc project $(NAMESPACE)
	@oc delete all -l template=$(APP_NAME)-client
