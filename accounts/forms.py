from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Vendor

class CustomerSignUpForm(UserCreationForm):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone_number = forms.IntegerField()
    gender = forms.CharField(choices=GENDER)
    profile_image = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password1', 'password2', 'address', 'phone_number', 'gender', 'profile_image')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(
                user = user, 
                first_name = self.cleaned_data.get('first_name'), 
                last_name = self.cleaned_data.get('last_name'),
                address = self.cleaned_data.get('address'), 
                phone_number = self.cleaned_data.get('phone_number'), 
                gender = self.cleaned_data.get('gender'), 
                profile_image = self.cleaned_data.get('profile_image'), 
            )
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
