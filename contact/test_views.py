from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import contact


class TestContactViews(SimpleTestCase):

    def test_view_contact_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
