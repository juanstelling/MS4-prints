from django.test import TestCase
from .models import Product, Category


class testCategoryModel(TestCase):

    def setUp(self):
        Category.objects.create(
            name='test name',
            friendly_name='test friendly name'
        )

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_friendly_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_friendly_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)


class TestProductModel(TestCase):

    def setUp(self):
        Product.objects.create(
            sku='test sku',
            name='test name',
            description='description',
            price=10.74
        )

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_sku_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('sku').verbose_name
        self.assertEqual(field_label, 'sku')

    def test_sku_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('sku').max_length
        self.assertEqual(max_length, 40)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 5)

    def test_image_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_image_url_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEqual(field_label, 'image url')

    def test_image_url_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('image_url').max_length
        self.assertEqual(max_length, 1024)

    def test_in_stock_booleanfield(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.in_stock)
