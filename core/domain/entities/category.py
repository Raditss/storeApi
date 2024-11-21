from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Category:
    id: Optional[int]
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None