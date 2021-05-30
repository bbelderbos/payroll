from datetime import datetime
from dataclasses import dataclass, field

from .payment import Payment


@dataclass
class Payroll:
    year: int
    month: int
    created: datetime = None
    log: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.created = datetime.now()

    @property
    def period(self):
        month = str(self.month).zfill(2)
        return f"{self.year}{month}"

    def pay(self, timesheets):
        for ts in timesheets:
            ts.payroll = self
            ts.paid = True
            pm = Payment(employee=ts.employee,
                         amount=ts.calculate_due(),
                         date_paid=datetime.now())
            self.log.append(pm)
