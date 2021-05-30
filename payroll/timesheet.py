from decimal import Decimal
from dataclasses import dataclass

from .employee import Employee


@dataclass
class TimeSheet:
    employee: Employee
    work_hours: int
    overwork_hours: int
    vacation_hours: int
    advancement: Decimal = 0
    saved: Decimal = 0
    due: Decimal = 0
    paid: bool = False

    def __post_init__(self):
        if not self.employee.active:
            raise RuntimeError(
                "Only active employees can submit timesheets")

    def _calculate_base_pay(self, em):
        if em.fixed:
            return em.fixed
        return self.work_hours * em.salary

    def _calculate_overwork(self, em):
        if em.fixed:
            return 0
        rate = em.company.overwork_rate
        return self.overwork_hours * rate

    def _calculate_saving(self, em, base_pay):
        if not em.does_saving:
            return 0
        perc = em.company.savings_percentage
        return perc * base_pay

    def calculate_pay(self):
        em = self.employee
        base_pay = self._calculate_base_pay(em)
        overwork = self._calculate_overwork(em)
        self.saved = self._calculate_saving(em, base_pay)
        self.due = (base_pay + overwork -
                    self.saved - self.advancement)
