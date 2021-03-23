from django.test import TestCase


class TestPagesViews(TestCase):

    """ All pages view testing  """

    def test_comapny_view(self):
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/company.html')

    def test_sustainability_view(self):
        response = self.client.get('/sustainability/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/sustainability.html')

    def test_faq_view(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/faq.html')

    def test_return_policy_view(self):
        response = self.client.get('/return-policy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/return_policy.html')
