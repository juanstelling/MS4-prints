from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import company, sustainability, faq, return_policy


class TestPagesViews(SimpleTestCase):

    def test_view_company_resolves(self):
        url = reverse('company')
        self.assertEqual(resolve(url).func, company)

    def test_view_sustainability_resolves(self):
        url = reverse('sustainability')
        self.assertEqual(resolve(url).func, sustainability)

    def test_view_faq_resolves(self):
        url = reverse('faq')
        self.assertEqual(resolve(url).func, faq)

    def test_view_return_policy_resolves(self):
        url = reverse('return_policy')
        self.assertEqual(resolve(url).func, return_policy)
