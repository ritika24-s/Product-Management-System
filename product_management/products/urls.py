from django.urls import path

from .views import *

urlpatterns = [
    path('', list_products, name="list_products"),
    path('add/', add_product, name="add_product"),
    path('edit/<int:product_id>', edit_product, name="edit_product"),
    path('delete/<int:product_id>', delete_product, name="delete_product"),
]