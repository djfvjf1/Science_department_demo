import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from tables.models import TeachersAddInfo


class Command(BaseCommand):
    help = 'Create users and user profiles from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                password = 'test'
                name = row.get('name', '').strip()  # Use get method and strip to handle missing or whitespace
                surname = row.get('surname', '').strip()
                username = row.get('email', '').strip()
                degree = row.get('degree', '').strip()
                position = row.get('position', '').strip()
                school = row.get('school', '').strip()

                user = User.objects.create_user(username=username, password=password)
                user_profile = TeachersAddInfo(user=user, avatar='static/profile/avatars/User-Profile-PNG-Clipart-1781504426.jpeg', name=name, surname=surname, degree=degree, position=position, school=school)
                user_profile.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))