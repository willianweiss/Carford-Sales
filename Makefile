lint:
	black . --line-length 79 -t py37 --skip-string-normalization
	isort . --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

test: ## Run tests
	pytest .

build: ## Build this project
	docker-compose build

down: ## Stop and remove all containers
	docker-compose down

up: ## Up all containers
	docker-compose up -d