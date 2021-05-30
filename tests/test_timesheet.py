from decimal import Decimal

import pytest

from payroll.timesheet import TimeSheet

EXPECTED_SALARIES = [
    Decimal(x) for x in (50, 200, 450, 800, 1250, 1800, 2450)]


@pytest.fixture
def timesheets(employees):
    timesheets = []
    for i, employee in enumerate(
        employees, start=1
    ):
        timesheets.append(
            TimeSheet(employee, i*5)
        )
    return timesheets


def test_no_timesheet_for_inactive_employee(employees, timesheets):
    empl = employees[-1]
    empl.active = False
    with pytest.raises(RuntimeError):
        TimeSheet(empl, 10)


@pytest.mark.parametrize("idx, saved, due", zip(
    range(7),
    [0] * 7,
    EXPECTED_SALARIES
))
def test_timesheet_base(employees, timesheets, idx, saved, due):
    ts = timesheets[idx]
    ts.calculate_pay()
    assert ts.saved == saved
    assert ts.due == due
    assert ts.paid is False


def test_timesheet_fixed_rates(employees):
    ceos = employees[:2]
    timesheets = []
    for ceo in ceos:
        ceo.fixed_rate = 5_000
        ts = TimeSheet(ceo, 40)
        ts.calculate_pay()
        timesheets.append(ts)
    assert all(ts.due == 5_000 for ts in timesheets)


def test_timesheet_savings_hourly(employees):
    empl = employees[0]
    empl.does_saving = True
    empl.hourly_rate = 100
    empl.fixed_rate = 0
    ts = TimeSheet(empl, 50)
    ts.calculate_pay()
    assert ts.due == Decimal(4_000)
    assert ts.saved == Decimal(1_000)


def test_timesheet_savings_fixed(employees):
    empl = employees[-1]
    empl.does_saving = True
    empl.hourly_rate = 0
    empl.fixed_rate = 1_000
    ts = TimeSheet(empl, 40)
    ts.calculate_pay()
    assert ts.due == Decimal(800)
    assert ts.saved == Decimal(200)
