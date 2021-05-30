from decimal import Decimal

from payroll.employee import Employee


def test_company(company):
    assert company.name == "PyBites"


def test_employee(company, employee):
    expected = Employee(
        name='Tim', company=company,
        hourly_rate=Decimal('50'), active=True)

    assert employee == expected


def test_payroll(payroll):
    assert payroll.period == "202105"
    assert payroll.log == []
