from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import email_list_signup


class TestNewsletterViews(SimpleTestCase):

    def test_email_list_signup_resolves(self):
        url = reverse('email_list_signup')
        self.assertEqual(resolve(url).func, email_list_signup)
