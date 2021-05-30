from decimal import Decimal

import pytest

from payroll.company import Company
from payroll.employee import Employee
from payroll.payroll import Payroll
from payroll.timesheet import TimeSheet


@pytest.fixture
def company():
    return Company("PyBites", Decimal(0.2), Decimal(1.5))


@pytest.fixture
def employee(company):
    return Employee(
        name="Tim",
        company=company,
        hourly_rate=Decimal(50)
    )


@pytest.fixture
def saving_employee(company):
    return Employee(
        name="Sara",
        company=company,
        hourly_rate=Decimal(60),
        saves=True
    )


@pytest.fixture
def timesheet(employee):
    return TimeSheet(employee=employee,
                     hours_worked=10)


@pytest.fixture
def timesheet_with_saves(saving_employee):
    return TimeSheet(employee=saving_employee,
                     hours_worked=10)


@pytest.fixture
def payroll(timesheet, timesheet_with_saves):
    return Payroll(year=2021, month=5,
                   timesheets=[timesheet,
                               timesheet_with_saves])
