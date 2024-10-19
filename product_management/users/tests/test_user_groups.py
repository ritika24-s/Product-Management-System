from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from products.models import Product
from users.models import User

class UserRolesTestCase(TestCase):
    def setUp(self):
        # Create user groups
        self.buyer_group, _ = Group.objects.get_or_create(name='Buyer')
        self.supplier_group, _ = Group.objects.get_or_create(name='Supplier')
        self.admin_group, _ = Group.objects.get_or_create(name='Administrator')

        content_type = ContentType.objects.get_for_model(Product)

        # Create permission for product viewing, editing and assigning it to groups
        view_permission = Permission.objects.get(codename='can_view_product', content_type=content_type)
        self.buyer_group.permissions.add(view_permission)
        self.supplier_group.permissions.add(view_permission)
        self.admin_group.permissions.add(view_permission)

        edit_permission = Permission.objects.get(codename='can_edit_product', content_type=content_type)
        self.supplier_group.permissions.add(edit_permission)

        # Create users
        self.buyer = User.objects.create_user(username='buyer', password='buyer123')
        self.supplier = User.objects.create_user(username='supplier', password='supplier123')
        self.admin = User.objects.create_superuser(username='admin', password='admin123')

        # Assign users to groups
        self.buyer.groups.add(self.buyer_group)
        self.supplier.groups.add(self.supplier_group)
        self.admin.groups.add(self.admin_group)

    def test_buyer_group_exists(self):
        self.assertTrue(Group.objects.filter(name='Buyer').exists())

    def test_supplier_group_exists(self):
        self.assertTrue(Group.objects.filter(name='Supplier').exists())

    def test_admin_group_exists(self):
        self.assertTrue(Group.objects.filter(name='Administrator').exists())

    def test_buyer_is_in_buyer_group(self):
        self.assertTrue(self.buyer.groups.filter(name='Buyer').exists())

    def test_supplier_is_in_supplier_group(self):
        self.assertTrue(self.supplier.groups.filter(name='Supplier').exists())

    def test_admin_is_in_admin_group(self):
        self.assertTrue(self.admin.groups.filter(name='Administrator').exists())

    def test_buyer_group_permissions(self):
        """Test if the buyer group has can_view_product permission"""
        permissions = self.buyer_group.permissions.all()
        self.assertTrue(permissions.filter(codename='can_view_product').exists())

    def test_user_permission_assignment(self):
        """Test if a user in the buyer group has correct permissions"""
        self.assertTrue(self.buyer.has_perm('products.can_view_product'))

    def test_supplier_group_permissions(self):
        """Test if the buyer group has can_view_product permission"""
        permissions = self.supplier_group.permissions.all()
        self.assertTrue(permissions.filter(codename='can_view_product').exists())
        self.assertTrue(permissions.filter(codename='can_edit_product').exists())

    def test_admin_group_permissions(self):
        """Test if the admin group has all permissions"""
        admin_permissions = Permission.objects.all()
        self.admin_group.permissions.set(admin_permissions)
        self.assertEqual(self.admin_group.permissions.count(), admin_permissions.count())

    def test_buyer_cannot_access_supplier_page(self):
        self.client.login(username='buyer', password='buyer123')
        response = self.client.get(reverse('supplier_product_list'))
        self.assertEqual(response.status_code, 302)