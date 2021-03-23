from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):

    def test_default_full_name_is_not_required(self):
        form = UserProfileForm({
            'default_full_name': ''})
        self.assertTrue(form.is_valid())

    def test_default_phone_number_is_not_required(self):
        form = UserProfileForm({'default_phone_number': ''})
        self.assertTrue(form.is_valid())

    def test_default_postcode_is_not_required(self):
        form = UserProfileForm({'default_postcode': ''})
        self.assertTrue(form.is_valid())

    def test_default_town_or_city_is_not_required(self):
        form = UserProfileForm({'default_town_or_city': ''})
        self.assertTrue(form.is_valid())

    def test_default_street_address1_is_not_required(self):
        form = UserProfileForm({'default_street_address1': ''})
        self.assertTrue(form.is_valid())

    def test_default_street_address2_is_not_required(self):
        form = UserProfileForm({'default_street_address2': ''})
        self.assertTrue(form.is_valid())

