from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_code', 'price', 'stock_status', 'supplier', "has_image", "images")
    search_fields = ('name', 'product_code', 'supplier')

admin.site.register(Product, ProductAdmin)
