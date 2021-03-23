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
