from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import all_products, product_detail, add_product


class TestProfilesViews(SimpleTestCase):

    def test_view_all_products_resolves(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_view_product_detail_resolves(self):
        url = reverse('product_detail', args=['product_id'])
        self.assertEqual(resolve(url).func, product_detail)

    def test_view_add_product_resolves(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)





