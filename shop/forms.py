from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'gender', 'address', 'email', 'password1', 'password2']

