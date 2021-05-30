from decimal import Decimal
from dataclasses import dataclass

from .company import Company


@dataclass(frozen=True)
class Employee:
    name: str
    company: Company
    hourly_rate: Decimal
    active: bool = True
    saves: bool = False
