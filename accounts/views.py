from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView
)
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, Vendor, User
from .forms import (
    CustomerRegisterForm, VendorRegisterForm,
    CustomerProfileUpdateForm, VendorProfileUpdateForm
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'accounts/customer_register.html'
    success_url = reverse_lazy('customer_login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_customer = True
        user.save()
        Customer.objects.create(user=user)
        return super().form_valid(form)

class VendorRegisterView(CreateView):
    model = User
    form_class = VendorRegisterForm
    template_name = 'accounts/vendor_register.html'
    success_url = reverse_lazy('vendor_login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_vendor = True
        user.save()
        Vendor.objects.create(user=user)
        return super().form_valid(form)

class CustomerLoginView(LoginView):
    template_name = 'accounts/customer_login.html'
    # success_url = reverse_lazy('customer_profile')

    def get_success_url(self):
        return reverse_lazy('customer_profile')

class VendorLoginView(LoginView):
    template_name = 'accounts/vendor_login.html'

    def get_success_url(self):
        return reverse_lazy('vendor_profile')

class CustomerLogoutView(LogoutView):
    next_page = reverse_lazy('customer_login')

class VendorLogoutView(LogoutView):
    next_page = reverse_lazy('vendor_login')

class CustomerPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/customer_password_change.html'
    success_url = reverse_lazy('customer_profile')

class VendorPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/vendor_password_change.html'
    success_url = reverse_lazy('vendor_profile')

class CustomerPasswordResetView(PasswordResetView):
    template_name = 'accounts/customer_password_reset.html'
    success_url = reverse_lazy('customer_login')

class VendorPasswordResetView(PasswordResetView):
    template_name = 'accounts/vendor_password_reset.html'
    success_url = reverse_lazy('vendor_login')

class CustomerProfileView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'accounts/customer_profile.html'

    # def get_object(self):
    #     return self.request.user.customer
    def get_object(self):
        return get_object_or_404(Customer, user=self.request.user)


class VendorProfileView(LoginRequiredMixin, DetailView):
    model = Vendor
    template_name = 'accounts/vendor_profile.html'

    # def get_object(self):
    #     return self.request.user.vendor
    
    def get_object(self):
        return get_object_or_404(Vendor, user=self.request.user)

class CustomerProfileUpdateView(UpdateView):
    model = Customer
    form_class = CustomerProfileUpdateForm
    template_name = 'accounts/customer_profile_update.html'
    success_url = reverse_lazy('customer_profile')

    def get_object(self):
        return self.request.user.customer

class VendorProfileUpdateView(UpdateView):
    model = Vendor
    form_class = VendorProfileUpdateForm
    template_name = 'accounts/vendor_profile_update.html'
    success_url = reverse_lazy('vendor_profile')

    def get_object(self):
        return self.request.user.vendor


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'accounts/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_register')

    def get_object(self):
        return self.request.user.customer
    
    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        user = customer.user
        customer.delete()
        user.delete()
        return super().delete(request, *args, **kwargs)
    

class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    template_name = 'accounts/vendor_confirm_delete.html'
    success_url = reverse_lazy('vendor_register')

    def get_object(self):
        return self.request.user.vendor

    def delete(self, request, *args, **kwargs):
        vendor = self.get_object()
        user = vendor.user
        vendor.delete()
        user.delete()
        return super().delete(request, *args, **kwargs)