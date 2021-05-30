from dataclasses import dataclass


@dataclass
class Company:
    name: str
    overwork_rate: float = 0
    savings_percentage: int = 0
