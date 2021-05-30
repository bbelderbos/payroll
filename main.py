from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Company:
    name: str
    overwork_rate: float = 0
    savings_percentage: int = 0


@dataclass
class Employee:
    id: int
    company_id: int
    name: str
    salary: int
    hourly: bool = True
    fixed: int = 0
    active: bool = True

    def __post_init__(self):
        if not self.hourly and self.fixed == 0:
            raise ValueError(
                "If not hourly employee set a fixed rate")


@dataclass
class TimeSheet:
    employee_id: int
    period: str
    work_hours: int
    overwork_hours: int
    vacation_hours: int
    advancement: Decimal = 0
    savings: Decimal = 0
    due: Decimal = 0
    paid: bool = False


class Payroll:

    def __init__(self, company period):
        self.timesheets = timesheets
        self.employee_balances = dict[Employee, int]

    def run(self):
        for ts in self.timesheets:
            ts.caculate()
            self.balances[
