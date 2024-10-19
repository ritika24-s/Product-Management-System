# products/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import Group

from users.models import Supplier, User
from products.models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a supplier user
        self.supplier_user = User.objects.create_user(username='supplier', password='supplier123', role='supplier')
        self.supplier_group, _ = Group.objects.get_or_create(name='Suppliers')
        self.supplier_user.groups.add(self.supplier_group)
        
        self.supplier = Supplier.objects.create(name="Test Supplier", user=self.supplier_user)
        self.product = Product.objects.create(
            supplier=self.supplier, name="Test Product", product_code="TP123", price=10, stock_status=True
        )

    def test_supplier_cannot_create_duplicate_product_code(self):
        # Create the first product
        Product.objects.create(supplier=self.supplier, name='Product 1', product_code='ABC123', price=10.0, stock_status=True)

        # Try to create a second product with the same code, which should raise an error
        with self.assertRaises(Exception):
            Product.objects.create(supplier=self.supplier, name='Product 2', product_code='ABC123', price=20.0, stock_status=True)

    def test_product_str_representation(self):
        """Test the string representation of the Product model"""
        self.assertEqual(str(self.product), "Test Product sold by Test Supplier")