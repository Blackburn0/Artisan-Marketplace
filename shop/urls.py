from django.urls import path, include
from .views import HomeView, UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('user/', include('django.contrib.auth.urls')), # user url
    path('user/login/', UserLoginView.as_view(), name='user-login'), # user login url
    path('user/logout/', UserLogoutView.as_view(), name='user-logout'), # user logout url
    
    path('user/register/', UserRegisterView.as_view(), name='user-register'), # user regsitration url
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),

    path('user/profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
]
