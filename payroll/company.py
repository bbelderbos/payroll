from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Company:
    name: str
    save_percentage: Decimal
    overwork_rate: Decimal
