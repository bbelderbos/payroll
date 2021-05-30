from decimal import Decimal
from dataclasses import dataclass

from .company import Company


@dataclass
class Employee:
    name: str
    company: Company
    hourly_rate: Decimal = Decimal(0)
    fixed_rate: Decimal = Decimal(0)
    active: bool = True
    saves: bool = False

    def __post_init__(self):
        if self.hourly_rate == 0 and self.fixed_rate == 0:
            raise ValueError(
                "Employee needs to have a regular or a fixed rate")
        if self.fixed_rate > 0:
            self.hourly_rate = Decimal(0)
