from django.db import transaction
from .category_seeder import CategorySeeder
from .product_seeder import ProductSeeder

class DatabaseSeeder:
    def __init__(self):
        self.category_seeder = CategorySeeder()
        self.product_seeder = ProductSeeder()

    @transaction.atomic
    def seed(self, products_count: int = 50):
        # Clear existing data
        self.clear()

        # Seed categories first
        categories = self.category_seeder.seed()

        # Update product seeder with categories and seed products
        self.product_seeder.categories = categories
        self.product_seeder.seed(products_count)

    def clear(self):
        # Clear in reverse order of dependencies
        self.product_seeder.clear()
        self.category_seeder.clear()
