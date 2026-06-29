from dataclasses import dataclass
from typing import Optional

@dataclass
class PiSpec:
    cpu: str
    gpu: Optional[str] = None
    ram: Optional[str] = None
    storage: Optional[str] = None
    other: Optional[str] = None

@dataclass
class PiModel:
    model_name: str
    specs: PiSpec
    price_usd: Optional[float]
    release_year: Optional[int]

def era_of(year: Optional[int], current_year: int) -> str:
    if year is None:
        return "unknown"
    if year <= current_year - 2:
        return "older"
    if year <= current_year:
        return "current"
    return "future"

