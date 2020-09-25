compile-local:
	export COMPOSE_FILE=local.yml; docker-compose build

run-local:
	export COMPOSE_FILE=local.yml; docker-compose up

purge-local:
	export COMPOSE_FILE=local.yml; docker-compose down

flask-migrate:
	export COMPOSE_FILE=local.yml; docker-compose run --rm flask sh
	