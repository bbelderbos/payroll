from .employee import Employee
from .payment import Payment
from .timesheet import TimeSheet

class Payroll:

    def __init__(self, year, month, timesheets):
        self.year: int = year
        self.month: int = month
        self.timesheets: list[TimeSheet] = timesheets
        self.payments = list[Payment] = []

    @property
    def period(self):
        return f"{self.year}{str(self.month).zfill(2)}"

    def calculate(self):
        for ts in self.timesheets:
            ts.calculate_pay()

    def pay(self):
        for ts in self.timesheets:
            ts.paid = True
            self.payments.append(
                Payment(
                    self.period,
                    ts.employee,
                    ts.due)
            )
