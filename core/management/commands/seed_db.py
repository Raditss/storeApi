from django.core.management.base import BaseCommand
from core.infrastructure.django.seeders.database_seeder import DatabaseSeeder

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--products',
            type=int,
            default=50,
            help='Number of products to create'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear the database before seeding'
        )

    def handle(self, *args, **options):
        seeder = DatabaseSeeder()

        if options['clear']:
            self.stdout.write('Clearing database...')
            seeder.clear()
            self.stdout.write(self.style.SUCCESS('Database cleared!'))

        self.stdout.write('Seeding database...')
        seeder.seed(products_count=options['products'])
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
