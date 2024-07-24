from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from .models import User
from .forms import UserRegistrationForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'shop/home.html'

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration/register_user.html'
    success_url = reverse_lazy('login')