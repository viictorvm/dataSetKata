UID=$(shell id -u)
GID=$(shell id -g)
DOCKER_SERVICE=dataset

.PHONY: exec
exec:
	python -m tornado.autoreload main.py

.PHONY: start
start: stop erase build up

copy:
	pip freeze > requirements.txt

.PHONY: up
up: ## spin up environment
		UID=${UID} GID=${GID} docker-compose up -d

.PHONY: stop
stop:
		docker-compose stop

.PHONY: erase
erase:
		docker-compose down -v

.PHONY: build
build:
		docker-compose build && \
		docker-compose pull

.PHONY: bash
bash:
		docker exec -it  ${DOCKER_SERVICE} sh