import random
from decimal import Decimal
from typing import List
from django.db import transaction
from ..models import ProductModel, CategoryModel
from .base_seeder import BaseSeeder
from faker import Faker

fake = Faker()

class ProductSeeder(BaseSeeder):
    def __init__(self, categories: List[CategoryModel] = None):
        self.categories = categories or []

    @transaction.atomic
    def seed(self, count: int = 50) -> List[ProductModel]:
        if not self.categories:
            raise ValueError("Categories must be provided before seeding products")

        print(f"Seeding {count} products...")
        created_products = []

        for _ in range(count):
            product = ProductModel.objects.create(
                name=self._generate_product_name(),
                description=fake.text(max_nb_chars=200),
                price=self._generate_price(),
                category=random.choice(self.categories),
            )
            created_products.append(product)

        print(f"Created {len(created_products)} products")
        return created_products

    def clear(self) -> None:
        print("Clearing products...")
        ProductModel.objects.all().delete()

    def _generate_product_name(self) -> str:
        adjectives = ['Premium', 'Deluxe', 'Basic', 'Professional', 'Ultimate']
        nouns = ['Widget', 'Gadget', 'Tool', 'Device', 'System']
        return f"{random.choice(adjectives)} {random.choice(nouns)} {fake.uuid4()[:8]}"

    def _generate_price(self) -> Decimal:
        return Decimal(random.uniform(9.99, 999.99)).quantize(Decimal('0.01'))
