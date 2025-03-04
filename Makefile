.PHONY: install run test lint format clean docker-up docker-down pre-commit

install:
	pip install -r requirements.txt
	pre-commit install

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v

lint:
	ruff check app tests
	mypy app tests --strict

format:
	black app tests
	ruff check --fix app tests

pre-commit:
	pre-commit run --all-files

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-up-db:
	docker compose up -d mongodb

dev: docker-up-db
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
