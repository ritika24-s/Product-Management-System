from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# import User model
from users.models import User
from products.models import Product

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):

        # Create groups
        buyer_group, _ = Group.objects.get_or_create(name='Buyers')
        supplier_group, _ = Group.objects.get_or_create(name='Suppliers')
        admin_group, _ = Group.objects.get_or_create(name='Administrators')

        # Get content type for Product model
        ct = ContentType.objects.get_for_model(Product)

        # Assign permissions to groups
        try:
            buyer_permissions = Permission.objects.get(codename='can_view_product', content_type=ct)
            supplier_permissions = [
                Permission.objects.get(codename='can_add_product', content_type=ct),
                Permission.objects.get(codename='can_edit_product', content_type=ct),
                Permission.objects.get(codename='can_view_product', content_type=ct),
            ]
            # Admins get all permissions
            admin_permissions = Permission.objects.all()  
        except Permission.DoesNotExist:
        # If permission doesn't exist yet (e.g., due to migration order), exit
            return
        
        # Assign permissions to groups
        for permission in supplier_permissions:
            supplier_group.permissions.add(permission)

        buyer_group.permissions.add(buyer_permissions)
        # Assign permissions to groups
        for permission in admin_permissions:
            admin_group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('User groups and permissions created successfully.'))
