from django.core.management import BaseCommand

from school.models import Payments, CASH, Lesson, Course
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {
                'pay': '1000',
                'lesson': Lesson.objects.get(pk=1),
                'user': User.objects.get(pk=2),
                'method': CASH,
            },
            {'pay': '2000'},
            {'pay': '3000'},
            {'pay': '4000'},
            {'pay': '5000'},
            {
                'pay': '6000',
                'course': Course.objects.get(pk=1),
                'user': User.objects.get(pk=1),
            },

        ]
        payment_for_create = []
        for pay in payments_list:
            payment_for_create.append(Payments(**pay))

        Payments.objects.all().delete()
        Payments.objects.bulk_create(payment_for_create)
