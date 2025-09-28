from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a test user with default credentials'

    def handle(self, *args, **options):
        if not User.objects.filter(username='user@example.com').exists():
            User.objects.create_user(
                username='user@example.com',
                email='user@example.com',
                password='password123',
                first_name='Test',
                last_name='User'
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created test user "user@example.com" with password "password123"')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Test user "user@example.com" already exists')
            )
