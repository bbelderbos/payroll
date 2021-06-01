lint:
	flake8 payroll tests

test:
	pytest

coverage:
	pytest --cov=payroll

typing:
	mypy payroll tests
