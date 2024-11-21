from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class ProductFilter:
    category: Optional[str] = None
    price_min: Optional[Decimal] = None
    price_max: Optional[Decimal] = None