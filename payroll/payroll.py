from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .payment import Payment
from .timesheet import TimeSheet


@dataclass
class Payroll:
    year: int
    month: int
    timesheets: list[TimeSheet]
    created: Optional[datetime] = None

    def __post_init__(self):
        self.created = datetime.now()

    @property
    def period(self) -> str:
        month = str(self.month).zfill(2)
        return f"{self.year}{month}"

    def pay(self) -> list[Payment]:
        payments = []
        for ts in self.timesheets:
            if ts.paid:
                continue
            ts.payroll = self.period
            ts.paid = True
            pm = Payment(employee=ts.employee,
                         amount=ts.calculate_due(),
                         date_paid=datetime.now())
            payments.append(pm)
        return payments
