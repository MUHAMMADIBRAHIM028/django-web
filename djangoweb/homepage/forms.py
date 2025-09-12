from django import forms
from .models import UserInfo, Product

# ---------------- Existing form for UserInfo ----------------
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email', 'age']


# ---------------- New form for Product ----------------
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user_role', 'name', 'sku_id', 'description', 'price', 'discount']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
