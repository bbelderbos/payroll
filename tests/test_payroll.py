from decimal import Decimal

from pytest import approx

from payroll.payment import Payment


def test_payroll(payroll, timesheet, timesheet_with_saves):
    payroll.pay(
        [timesheet, timesheet_with_saves])
    assert timesheet.payroll == payroll
    assert timesheet.paid is True
    assert timesheet_with_saves.payroll == payroll
    assert timesheet_with_saves.paid is True
    assert type(payroll.log[0]) == Payment
    assert payroll.log[0].amount == Decimal(500)
    assert payroll.log[1].amount == approx(Decimal(480))
