import pytest

from payroll.company import Company
from payroll.employee import Employee
from payroll.timesheet import TimeSheet


@pytest.fixture
def company():
    return Company("PyBites", 1.25, 0.20)


@pytest.fixture
def employees(company):
    employees = []
    for i, name in enumerate(
        'julian bob tim sara joyce niki jill'.split(),
        start=1
    ):
        employees.append(
            Employee(i, name, company, i*10)
        )
    return employees
