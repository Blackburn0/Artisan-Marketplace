from django.urls import include, path
from .views import HomeView, StoreView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store')
]
