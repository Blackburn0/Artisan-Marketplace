# from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User, Vendor

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'profile_image', 'gender', 'address', 'email']

class VendorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
            Vendor.objects.create(user=user)
        return user