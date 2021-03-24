from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_product_form_is_required(self):
        form = ProductForm({
            'name': '',
            'description': '',
            'price': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_form_is_not_required(self):
        form = ProductForm({
            'sku': 'test sku',
            'category': 'category',
            'image': 'image',
            'image_url': 'image_url',
            'in_stock': 'in_stock'
            })
        self.assertTrue(form.is_valid)
