from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import index


class TestPagesViews(SimpleTestCase):

    def test_view_index_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)
