from django.db import models
from django.contrib.auth.models import User
#from django.db import models
from django.contrib.auth.models import AbstractUser

# ---------------- Existing UserInfo model ----------------
class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ---------------- New Product model ----------------
class Product(models.Model):
    ROLE_CHOICES = [
        ('', 'Select'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    PRODUCT_TYPES = [
        ('physical', 'Physical'),
        ('virtual', 'Virtual'),
    ]


    # Dropdown to select role
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # Name field
    name = models.CharField(max_length=100)
    # SKU ID field
    sku_id = models.CharField(max_length=50, unique=True)
    # Description field (large box)
    description = models.TextField()
    # Price field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Discount field
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPES,
        default='physical'

    )

    def __str__(self):
        return self.name
    #----------------------------signup form-----------------#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('shemale', 'Shemale')],
        null=True,
        blank=True
    )
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
        
