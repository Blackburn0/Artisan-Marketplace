from atexit import register
from django.urls import path, include
from .views import HomeView, UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserProfileUpdateView, UserProfileDeleteView, VendorRegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/login/', UserLoginView.as_view(), name='user-login'), # user login url
    path('user/logout/', UserLogoutView.as_view(), name='user-logout'), # user logout url
    path('user/register/', UserRegisterView.as_view(), name='user-register'), # user regsitration url
    path('user/profile/', UserProfileView.as_view(), name='user-profile'), # user profile page url
    path('user/profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'), # user profile update page url
    path('user/profile/delete/', UserProfileDeleteView.as_view(), name='user-profile-delete'), # user delete profile

    path('vendor/register/', VendorRegisterView.as_view(), name="vendor-register")
]
