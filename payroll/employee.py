from decimal import Decimal
from dataclasses import dataclass

from .company import Company


@dataclass
class Employee:
    id: int
    name: str
    company: Company
    hourly_rate: Decimal = 0
    fixed_rate: Decimal = 0
    active: bool = True
    does_saving: bool = False

    def __post_init__(self):
        if self.hourly_rate and self.fixed_rate:
            raise ValueError(
                "Employee has either hourly or fixed rate")
