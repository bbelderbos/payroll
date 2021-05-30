from datetime import datetime
from dataclasses import dataclass
from decimal import Decimal

from .employee import Employee


@dataclass
class Payment:
    employee: Employee
    amount: Decimal
    date_paid: datetime = None

    def __post_init__(self):
        self.date_paid = datetime.now()
