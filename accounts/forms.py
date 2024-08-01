from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Vendor

class CustomerSignUpForm(UserCreationForm):
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(user=user, address=self.cleaned_data.get('address'))
        return user

class VendorSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'company_name', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
            Vendor.objects.create(user=user, company_name=self.cleaned_data.get('company_name'), phone_number=self.cleaned_data.get('phone_number'))
        return user
