from typing import List
from django.db import transaction
from ..models import CategoryModel
from .base_seeder import BaseSeeder

class CategorySeeder(BaseSeeder):
    categories = [
        {"name": "Electronics"},
        {"name": "Clothing"},
        {"name": "Books"},
        {"name": "Home & Garden"},
        {"name": "Sports"},
        {"name": "Toys"},
        {"name": "Food & Beverages"},
        {"name": "Health & Beauty"},
        {"name": "Automotive"},
        {"name": "Office Supplies"}
    ]

    @transaction.atomic
    def seed(self) -> List[CategoryModel]:
        print("Seeding categories...")
        created_categories = []
        for category_data in self.categories:
            category, created = CategoryModel.objects.get_or_create(
                name=category_data["name"]
            )
            created_categories.append(category)
        print(f"Created {len(created_categories)} categories")
        return created_categories

    def clear(self) -> None:
        print("Clearing categories...")
        CategoryModel.objects.all().delete()