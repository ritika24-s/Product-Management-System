from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path("signup/", create_user, name="signup"),
    # Buyer section
    path('buyer/products/', buyer_product_list, name='buyer_product_list'),

    # Supplier section
    path('supplier/products/', supplier_product_list, name='supplier_product_list'),
    path('supplier/cheaper-analogues/', supplier_cheaper_analogues, name='supplier_cheaper_analogues'),
]

