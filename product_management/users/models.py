from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# pre-defined roles 
# Buyer - can view the product listing
# Supplier - can view the list of their products
# Administrator - access to the administrator interface

# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
        
        
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True')
        
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True')
        
#         return self.create_user(username, password, **extra_fields)
    

# User class
class User(AbstractUser):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('supplier', 'Supplier'),
        ('admin', 'Admin'),
    ]
    username = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="buyer")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # objects = UserManager()
    
    def __str__(self):
        return self.username
    
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supplier')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name