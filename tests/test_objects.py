from decimal import Decimal

import pytest

from payroll.employee import Employee


def test_company(company):
    assert company.name == "PyBites"


def test_employee(company, employee):
    expected = Employee(
        name='Tim', company=company,
        hourly_rate=Decimal('50'), active=True)
    assert employee == expected


def test_employee_validation(company, employee):
    with pytest.raises(ValueError):
        Employee(
            name='Jake', company=company,
            hourly_rate=Decimal('50'),
            fixed_rate=Decimal('3_000'))


def test_payroll(payroll):
    assert payroll.period == "202105"
    assert len(payroll.timesheets) == 2
    assert len(payroll.logs) == 0
