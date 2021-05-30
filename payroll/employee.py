from decimal import Decimal
from dataclasses import dataclass

from .company import Company


@dataclass
class Employee:
    id: int
    company: Company
    name: str
    salary: int
    hourly: bool = True
    fixed: int = 0
    active: bool = True
    does_saving: bool = False
    total_paid: Decimal = 0

    def __post_init__(self):
        if not self.hourly and self.fixed == 0:
            raise ValueError(
                "If not hourly employee set a fixed rate")
