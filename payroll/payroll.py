from .employee import Employee
from .timesheet import TimeSheet


class Payroll:

    def __init__(self, year, month, timesheets):
        self.year: int = year
        self.month: int = month
        self.timesheets: list[TimeSheet] = timesheets
        self.employee_balances = dict[Employee, int]

    def calculate(self):
        for ts in self.timesheets:
            ts.calculate_pay()
            self.balances[ts.employee] = ts.due

    def pay(self):
        for ts in self.timesheets:
            ts.paid = True
            # TODO add entry to payment table
