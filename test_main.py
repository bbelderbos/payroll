from decimal import Decimal

import pytest

from main import Employee

COMPANY_ID = 1


@pytest.fixture
def employees():
    names = 'tim sara jake'.split()
    salaries = [Decimal(i)*1_000 for i in (42, 57, 48)]
    employees = [Employee(i, COMPANY_ID, name, salary) for
                 i, (name, salary) in
                 enumerate(zip(names, salaries), start=1)]
    employees[-1].active = False
    return employees


def test_company_employees(employees):
    assert len(employees) == 3


def test_employee_rate_validation():
    expected_error = "If not hourly employee set a fixed rate"
    with pytest.raises(ValueError, match=expected_error):
        Employee(47, COMPANY_ID, 'Henry', 10_000, False)
    Employee(47, COMPANY_ID, 'Henry', 10_000, False, 100_000)
