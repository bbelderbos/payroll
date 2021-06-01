from decimal import Decimal

from pytest import approx


def test_payroll(payroll):
    payments = payroll.pay()
    period = "202105"
    assert all(ts.payroll == period
               for ts in payroll.timesheets)
    assert all(ts.paid is True
               for ts in payroll.timesheets)
    assert payments[0].amount == approx(Decimal('500.0'))
    assert payments[1].amount == approx(Decimal('480.0'))


def test_payroll_should_not_process_timesheets_twice(payroll):
    payments = payroll.pay()
    assert len(payments) == 2
    payments = payroll.pay()
    assert len(payments) == 0
