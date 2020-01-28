#!make

restart: stop | build | run

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

clean:
	@echo "+\n++ Removing containers, images, volumes etc...\n+"
	@docker-compose rm -f -v -s
	@docker volume rm -f react-python-starter_postgres-data
