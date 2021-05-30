from datetime import datetime
from dataclasses import dataclass, field

from .payment import Payment
from .timesheet import TimeSheet


@dataclass
class Payroll:
    year: int
    month: int
    timesheets: list[TimeSheet]
    created: datetime = None
    logs: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.created = datetime.now()

    @property
    def period(self):
        month = str(self.month).zfill(2)
        return f"{self.year}{month}"

    def pay(self):
        for ts in self.timesheets:
            ts.payroll = self.period
            ts.paid = True
            pm = Payment(employee=ts.employee,
                         amount=ts.calculate_due(),
                         date_paid=datetime.now())
            self.logs.append(pm)
