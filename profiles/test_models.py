from django.test import TestCase
from .models import UserProfile


class TestUserProfileModel(TestCase):

    def setUp(self):
        UserProfile.objects.create(
            default_full_name='test default full name',
            default_phone_number='test default full name',
            default_country='test country',
            default_postcode='test postcode',
            default_town_or_city='test town or city',
            default_street_address1='test street address1',
            default_street_address2='test street address2'
        )

    def test_user_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_default_full_name_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_full_name').verbose_name
        self.assertEqual(field_label, 'default full name')

    def test_default_full_name_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_full_name').max_length
        self.assertEqual(max_length, 50)

    def test_default_phone_number_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_phone_number').verbose_name
        self.assertEqual(field_label, 'default phone number')

    def test_default_phone_number_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_default_default_country_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_country').verbose_name
        self.assertEqual(field_label, 'default country')

    def test_default_country_blank_label(self):
        profile = UserProfile.objects.get(id=1)
        blank_label = profile._meta.get_field('default_country').blank_label
        self.assertEqual(blank_label, 'Country')

    def test_default_postcode_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_postcode').verbose_name
        self.assertEqual(field_label, 'default postcode')

    def test_default_postcode_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_postcode').max_length
        self.assertEqual(max_length, 20)

    def test_default_town_or_city_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_town_or_city').verbose_name
        self.assertEqual(field_label, 'default town or city')

    def test_default_town_or_city_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_town_or_city').max_length
        self.assertEqual(max_length, 40)

    def test_default_street_address1_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_street_address1').verbose_name
        self.assertEqual(field_label, 'default street address1')

    def test_default_street_address1_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field(
            'default_street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_default_street_address2_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_street_address2').verbose_name
        self.assertEqual(field_label, 'default street address2')

    def test_default_street_address2_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field(
            'default_street_address2').max_length
        self.assertEqual(max_length, 80)


