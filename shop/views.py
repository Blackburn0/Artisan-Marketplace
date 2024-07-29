from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import User, Vendor
from .forms import UserRegistrationForm, UserProfileUpdateForm, VendorRegistrationForm
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

class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy("home")

    def get_object(self):
        # Return the current logged-in user
        return self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    




class VendorRegisterView(CreateView):
    model = Vendor
    form_class = VendorRegistrationForm
    template_name = 'vendor/register_vendor.html'
    success_url = reverse_lazy('login')