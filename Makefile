.PHONY: lint
lint:
	flake8 payroll tests

.PHONY: typing
typing:
	mypy payroll tests

.PHONY: test
test:
	pytest --cov=payroll

.PHONY: ci
ci: lint typing test
