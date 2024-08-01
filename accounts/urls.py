from django.urls import path
from .views import CustomerSignUpView, VendorSignUpView

urlpatterns = [
    path('signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('signup/vendor/', VendorSignUpView.as_view(), name='vendor_signup'),
]
