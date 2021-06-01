# Payroll calculator

Going through the exercise of modeling a payroll system.

I am only using classes to stick to the business logic and not depend on any ORM or DB implementation.

TODO: actually add DB and web (Flask) layers.

## Setup

Create a virtual environment and install the dependencies:

```
pip install -r requirements/requirements.txt
```

To run the tests:

```
make test
```

To run the tests + mypy + flake8:

```
make ci
```

To make its pass a requirement before committing:

```
pre-commit install
```
