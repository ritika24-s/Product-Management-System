# Generated by Django 5.1.2 on 2024-10-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('can_view_product', 'Can view product'), ('can_add_product', 'Can add product'), ('can_edit_product', 'Can edit product'), ('can_delete_product', 'Can delete product'))},
        ),
    ]
