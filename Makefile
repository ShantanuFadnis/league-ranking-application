SHELL := /bin/bash

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}'

build-image: ## Build image for testing
	@docker-compose -f docker-compose.yml build

unittest: ## Run unit tests for the application
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e py37

flake8: ## Run flake8 tests for the application
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e flake8

pylint: ## Run pylint tests for the application
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e pylint

mypy: ## Run mypy tests for the application
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e mypy

black: ## Run black tests for the application
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e black

blacken: ## Format codebase using black
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e blacken

lint-all: ## Run all linter checks
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox -e flake8,pylint,mypy,black

test-all: build-image ## Run all tests
	@docker-compose -f docker-compose.yml run --entrypoint "" --rm --no-deps app tox

clear: ## Remove containers used in tests
	@docker-compose -f docker-compose.yml down -v --remove-orphans --rmi 'all' && rm -rf "output"

bash-in-container: ## Execute bash in container
	@docker-compose -f docker-compose.yml run app bash

run: ## Run application inside Docker
	docker-compose -f docker-compose.yml run --entrypoint "bin/run.sh ${input} output" --rm --no-deps app

run-local: ## Run application locally in a python virtual environment
	@source bin/run_local.sh "${input}" "output"

show-output: ## Show output produced after running the application
	cat output/*.txt
