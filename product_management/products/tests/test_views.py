from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group

from products.models import Product
from users.models import User, Supplier

class BuyerProductListingTestCase(TestCase):
    def setUp(self):       
        # Create buyer, supplier , and assign them to the appropriate groups
        self.buyer = User.objects.create_user(username='buyer', password='buyer123', role="buyer")
        self.buyer_group, _ = Group.objects.get_or_create(name='Buyers')
        self.buyer.groups.add(self.buyer_group)

        self.supplier_user = User.objects.create_user(username='supplier', password='supplier123', role='supplier')
        self.supplier_group, _ = Group.objects.get_or_create(name='Suppliers')
        self.supplier_user.groups.add(self.supplier_group)
        
        # Create supplier instance and products
        self.supplier = Supplier.objects.create(user=self.supplier_user, name='Supplier One')        
        Product.objects.create(supplier=self.supplier, name='Product 1', product_code='ABC123', price=100.00, stock_status=True)
        Product.objects.create(supplier=self.supplier, name='Product 2', product_code='XYZ456', price=200.00, stock_status=False)

    def test_buyer_sees_in_stock_products(self):
        # Log the buyer in
        self.client.login(username='buyer', password='buyer123')
        response = self.client.get(reverse('buyer_product_list'))
        self.assertContains(response, 'Product 1')  # In stock
        self.assertNotContains(response, 'Product 2')  # Out of stock

    def test_supplier_sees_own_products(self):
        self.client.login(username='supplier', password='supplier123')
        response = self.client.get(reverse('supplier_product_list'))
        self.assertContains(response, "Product 2")
