from decimal import Decimal
from dataclasses import dataclass


@dataclass(frozen=True)
class Company:
    name: str
    save_percentage: Decimal
    overwork_rate: Decimal
