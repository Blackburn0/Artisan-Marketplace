from django.urls import path
from .views import (
    CustomerRegisterView, VendorRegisterView,
    CustomerLoginView, VendorLoginView,
    CustomerLogoutView, VendorLogoutView,
    CustomerPasswordChangeView, VendorPasswordChangeView,
    CustomerPasswordResetView, VendorPasswordResetView,
    CustomerProfileView, VendorProfileView,
    CustomerProfileUpdateView, VendorProfileUpdateView,
    CustomerDeleteView, VendorDeleteView
)

urlpatterns = [
    # cutomer
    path('customer/register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('customer/login/', CustomerLoginView.as_view(), name='customer_login'),
    path('customer/logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('customer/password_change/', CustomerPasswordChangeView.as_view(), name='customer_password_change'),
    path('customer/password_reset/', CustomerPasswordResetView.as_view(), name='customer_password_reset'),
    path('customer/profile/', CustomerProfileView.as_view(), name='customer_profile'),
    path('customer/profile_update/', CustomerProfileUpdateView.as_view(), name='customer_profile_update'),
    path('customer/profile_delete/', CustomerDeleteView.as_view(), name='customer_profile_delete'),


    # vendor
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor_register'),
    path('vendor/login/', VendorLoginView.as_view(), name='vendor_login'),
    path('vendor/logout/', VendorLogoutView.as_view(), name='vendor_logout'),
    path('vendor/password_change/', VendorPasswordChangeView.as_view(), name='vendor_password_change'),
    path('vendor/password_reset/', VendorPasswordResetView.as_view(), name='vendor_password_reset'),
    path('vendor/profile/', VendorProfileView.as_view(), name='vendor_profile'),
    path('vendor/profile_update/', VendorProfileUpdateView.as_view(), name='vendor_profile_update'),
    path('vendor/profile_delete/', VendorDeleteView.as_view(), name='vendor_profile_delete'),

]
