from django.db import models
from users.models import Supplier

 
# creating an django model class
class Product(models.Model):
    # supplier field populated using Supplier database
    supplier = models.ForeignKey(Supplier, on_delete= models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, null=False)
    product_code = models.CharField(max_length=200)
    price = models.IntegerField()
    stock_status = models.BooleanField(default=True)  # True = In stock, False = Out of stock
    # images field (optional, one marked as main/default if it exists)
    images = models.ImageField(upload_to='product_images/', blank=True, null=True)
    main_image = models.BooleanField(default=False)
    
    # meta for the class
    class Meta:
        # Each supplier can only have one product with a specific code
        constraints = [
            models.UniqueConstraint(fields=['supplier', 'product_code'], name='unique_product_code_per_supplier')
        ]  
        
        permissions = [
            ("can_view_product", "Can view product"),
            ("can_add_product", "Can add product"),
            ("can_edit_product", "Can edit product"),
            ("can_delete_product", "Can delete product"),
        ]

    # used while managing models from terminal
    def __str__(self):
        return f"{self.name} sold by {self.supplier.name}"
    
    def has_image(self):
        return bool(self.images)