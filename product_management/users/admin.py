from django.contrib import admin
from .models import User, Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

# Register your models here.
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(User)