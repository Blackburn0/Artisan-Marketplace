from django.urls import path, include
from .views import HomeView, UserRegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/register/', UserRegisterView.as_view(), name='user-register'), # user regsitration url
    path('user/', include('django.contrib.auth.urls')), # user login url

]
