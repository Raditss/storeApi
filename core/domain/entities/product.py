from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from typing import Optional

@dataclass
class Product:
    id: Optional[int]
    name: str
    description: Optional[str]
    price: Decimal
    category_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
