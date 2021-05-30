from decimal import Decimal
from dataclasses import dataclass

from .employee import Employee


@dataclass
class TimeSheet:
    employee: Employee
    hours_worked: int
    overwork_hours: int = 0
    advancements: Decimal = 0
    paid: bool = False
    payroll: str = None

    def __post_init__(self):
        self.company = self.employee.company
        self.base_pay = (self.employee.hourly_rate *
                         self.hours_worked)

    def calculate_overwork(self):
        return (self.employee.hourly_rate *
                self.company.overwork_rate * self.overwork_hours)

    def calculate_saving(self):
        if not self.employee.saves:
            return 0
        return self.company.save_percentage * self.base_pay

    def calculate_due(self):
        return (self.base_pay +
                self.calculate_overwork() -
                self.calculate_saving() -
                self.advancements)
