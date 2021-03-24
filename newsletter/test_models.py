from django.test import TestCase
from .models import Subscribe


class TestSubscribeeModel(TestCase):

    def setUp(self):
        Subscribe.objects.create(
            email='test_full_name',
            timestamp='test@email.com',
        )

    def test_email_label(self):
        subscribe = Subscribe.objects.get(id=1)
        field_label = subscribe._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_timestamp_label(self):
        subscribe = Subscribe.objects.get(id=1)
        field_label = subscribe._meta.get_field('timestamp').verbose_name
        self.assertEqual(field_label, 'timestamp')
