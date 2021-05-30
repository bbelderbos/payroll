from decimal import Decimal

from pytest import approx


def test_payroll(payroll):
    payroll.pay()
    period = "202105"
    assert all(ts.payroll == period
               for ts in payroll.timesheets)
    assert all(ts.paid is True
               for ts in payroll.timesheets)
    assert payroll.log[0].amount == Decimal(500)
    assert payroll.log[1].amount == approx(Decimal(480))
