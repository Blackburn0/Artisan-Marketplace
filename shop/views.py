from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from .models import User
from .forms import UserRegistrationForm, UserProfileUpdateForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = 'shop/home.html'

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register_user.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'user/login_user.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_profile.html'
    
    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user-profile')

    def get_object(self):
        return self.request.user
