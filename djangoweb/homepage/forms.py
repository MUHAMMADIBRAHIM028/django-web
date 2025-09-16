# homepage/forms.py
from django import forms
from .models import UserInfo, Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email', 'age']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user_role', 'name', 'sku_id', 'description', 'price', 'discount']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        max_length=254, required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Apply bootstrap styling
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control', 'placeholder': fieldname.replace('password', 'Password')})
            self.fields[fieldname].help_text = ''