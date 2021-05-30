from decimal import Decimal

import pytest

from payroll.payroll import Payroll
from payroll.timesheet import TimeSheet


def test_company_employees(employees):
    assert len(employees) == 7
