from django.core.management.base import BaseCommand
from core.infrastructure.django.seeders.database_seeder import DatabaseSeeder

class Command(BaseCommand):
    help = 'Clear all data from the database'

    def handle(self, *args, **options):
        self.stdout.write('Clearing database...')
        seeder.clear()
        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
