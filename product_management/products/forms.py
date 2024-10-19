from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Fields to include in form
        fields = ['name', 'product_code', 'price', 'stock_status', 'images']

    def __init__(self, *args, **kwargs):
        self.supplier = kwargs.pop('supplier', None)
        super(ProductForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        product = super().save(commit=False)
        if self.supplier:
            product.supplier = self.supplier
        if commit:
            product.save()
        return product
