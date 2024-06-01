from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='moder@retail.pro',
            first_name='moder',
            last_name='moder',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password('123qaz')
        user.save()
