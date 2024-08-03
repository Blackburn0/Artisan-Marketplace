from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Vendor

class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VendorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'phone']

class VendorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['company_name', 'phone']
