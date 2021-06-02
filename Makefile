.PHONY: setup
setup:
	python3.9 -m venv venv && source venv/bin/activate && pip install -r requirements/requirements.txt

.PHONY: lint
lint:
	flake8 payroll tests

.PHONY: typing
typing:
	mypy payroll tests

.PHONY: test
test:
	pytest

.PHONY: coverage
coverage:
	pytest --cov=payroll

.PHONY: ci
ci: lint typing test
