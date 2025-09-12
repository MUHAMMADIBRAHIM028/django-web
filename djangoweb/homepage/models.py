from django.db import models

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
        ('Admin', 'Admin'),
        ('User', 'User'),
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

    def __str__(self):
        return self.name
