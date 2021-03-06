from decimal import Decimal

import pytest

from payroll import Employee, Payroll


def test_company(company):
    assert company.name == "PyBites"


def test_employee(company, employee):
    expected = Employee(
        name='Tim', company=company,
        hourly_rate=Decimal('50'), active=True)
    assert employee == expected


def test_employee_rate_validation(company):
    expected_error = (
        "Employee needs to have a regular or a fixed rate")
    with pytest.raises(ValueError, match=expected_error):
        Employee(
            name='Jake', company=company,
            hourly_rate=Decimal(0),
            fixed_rate=Decimal(0))


def test_contractor_zeros_hourly(contractor):
    contractor.fixed_rate = Decimal(3_000)
    assert contractor.hourly_rate == 0


def test_payroll(payroll):
    assert payroll.period == "202105"
    assert len(payroll.timesheets) == 2


def test_payroll_created_date_is_not_static():
    pr1 = Payroll(2021, 5, [])
    pr2 = Payroll(2021, 5, [])
    assert pr2.created > pr1.created
