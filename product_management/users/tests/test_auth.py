# tests/test_auth.py
from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRoleTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin123', is_staff=True)
        self.supplier = User.objects.create_user(username='supplier', password='supplier123')
        self.buyer = User.objects.create_user(username='buyer', password='buyer123')

    def test_admin_login(self):
        response = self.client.login(username='admin', password='admin123')
        self.assertTrue(response)

    def test_supplier_login(self):
        response = self.client.login(username='supplier', password='supplier123')
        self.assertTrue(response)

    def test_buyer_login(self):
        response = self.client.login(username='buyer', password='buyer123')
        self.assertTrue(response)
