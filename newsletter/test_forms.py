from django.test import TestCase
from .forms import EmailSubscribeForm


class TestNewsletterForm(TestCase):

    def test_newsletter_form_is_required(self):
        form = EmailSubscribeForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
