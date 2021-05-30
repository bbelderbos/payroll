from dataclasses import dataclass
from datetime import datetime
from itertools import count

from .employee import Employee

cnt = count(start=1)


@dataclass
class Payment:
    id: int = 0
    period: str
    employee: Employee
    amount: int
    added: datetime = None

    def __post_init__(self):
        self.id = next(cnt)
        self.added = datetime.now()
