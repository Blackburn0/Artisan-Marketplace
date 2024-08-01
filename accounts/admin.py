from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, Vendor

class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False

class VendorInline(admin.StackedInline):
    model = Vendor
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (CustomerInline, VendorInline)
    list_display = ('username', 'is_customer', 'is_vendor')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Vendor)
