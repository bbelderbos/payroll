import pytest

from payroll.company import Company
from payroll.employee import Employee


@pytest.fixture
def company():
    return Company("PyBites", 1.25, 0.25)


@pytest.fixture
def employees(company):
    employees = []
    for i, name in enumerate(
        'julian bob tim sara joyce niki jill'.split(),
        start=1
    ):
        employees.append(
            Employee(i, company, name, i*10_000)
        )

    for ceo in employees[:2]:
        ceo.hourly = False
        ceo.fixed = 25_000
    for e in employees[::2]:
        e.does_saving = True
    employees[-1].active = False
    return employees
