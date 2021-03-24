from django.test import TestCase
from .models import ContactMessage


class TestContactMessageModel(TestCase):

    def setUp(self):
        ContactMessage.objects.create(
            full_name='test_full_name',
            email='test@email.com',
            message='test message'
        )

    def test_full_name_label(self):
        message = ContactMessage.objects.get(id=1)
        field_label = message._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_full_name_max_length_label(self):
        message = ContactMessage.objects.get(id=1)
        max_length = message._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_label(self):
        message = ContactMessage.objects.get(id=1)
        field_label = message._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_message_label(self):
        message = ContactMessage.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')
