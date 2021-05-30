from decimal import Decimal

import pytest

from payroll import Company
from payroll import Employee
from payroll import Payroll
from payroll import TimeSheet


@pytest.fixture
def company():
    return Company(
        name="PyBites",
        save_percentage=Decimal(0.2),
        overwork_rate=Decimal(1.5))


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
def contractor(company):
    return Employee(
        name="Jake",
        company=company,
        fixed_rate=Decimal(3_000),
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
def timesheet_fixed_rate(contractor):
    return TimeSheet(employee=contractor,
                     hours_worked=200)


@pytest.fixture
def payroll(timesheet, timesheet_with_saves):
    timesheets = [timesheet, timesheet_with_saves]
    return Payroll(year=2021, month=5,
                   timesheets=timesheets)
