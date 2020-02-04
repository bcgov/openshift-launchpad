#!make

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

clean:
	@echo "+\n++ Removing containers, images, volumes etc..."
	@echo "+\n++ Note: does not clear image cache \n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f openshift-launchpad_postgres-data

db-upgrade:
	@echo "+\n++ Running database migrations \n+"
	@docker-compose restart server-migrate