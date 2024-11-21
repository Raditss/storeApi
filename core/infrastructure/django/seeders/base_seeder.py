from typing import List
from django.db import transaction

class BaseSeeder:
    @transaction.atomic
    def seed(self) -> None:
        raise NotImplementedError("Seed method must be implemented")

    def clear(self) -> None:
        raise NotImplementedError("Clear method must be implemented")