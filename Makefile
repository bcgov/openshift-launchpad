#!make

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

openshift-server-build:
	@echo "+\n++ Creating OpenShift build config and image stream...\n+"
	@oc process -f deployment/server.bc.json | oc create --validate -f -

openshift-server-deploy:
	test -n "$(NAMESPACE)" # Please provide a namespace via NAMESPACE=mynamespace
	@echo "+\n++ Creating OpenShift deployment config, services, and routes...\n+"
	@oc process -f deployment/server.dc.json -p NAMESPACE=$(NAMESPACE) | oc create --validate -f -

openshift-server-clean:
	@echo "+\n++ Tearing down OpenShift objects created from templates...\n+"
	@oc delete all -l template=openshift-launchpad
