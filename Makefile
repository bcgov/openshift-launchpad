#!make

restart: stop | build | run
setup: update-submodules | reinitialize-git

build:
	@echo "+\n++ Building images ...\n+"
	@docker-compose build --parallel

run:
	@echo "+\n++ Running client and server ...\n+"
	@docker-compose up -d

run-server:
	@echo "+\n++ Running server ...\n+"
	@docker-compose up -d server

stop:
	@echo "+\n++ Stopping client and server ...\n+"
	@docker-compose down -t 2

db-seed:
	@echo "+\n++ Seeding database ...\n+"
	@docker-compose run server python manage.py seed-db

server-test:
	@echo "+\n++ Running server unit tests ...\n+"
	@docker-compose run server python manage.py test

client-test:
	@echo "+\n++ Running client unit tests ...\n+"
	@docker-compose run client npm test

clean:
	@echo "+\n++ Removing containers, images, volumes etc...\n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f react-python-starter_postgres-data

update-submodules:
	@echo "+\n++ Updating submodules ...\n+"
	@mkdir -p client && cd ./client && git submodule init && git submodule update

reinitialize-git:
	@rm .gitmodules
	@rm -rf .github
	@rm -rf .git
	@rm -rf ./client/.git
	@git init
