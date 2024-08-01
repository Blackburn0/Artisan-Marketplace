from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import CustomerSignUpForm, VendorSignUpForm

class CustomerSignUpView(View):
    def get(self, request):
        form = CustomerSignUpForm()
        return render(request, 'accounts/signup_form.html', {'form': form})

    def post(self, request):
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup_form.html', {'form': form})

class VendorSignUpView(View):
    def get(self, request):
        form = VendorSignUpForm()
        return render(request, 'accounts/signup_form.html', {'form': form})

    def post(self, request):
        form = VendorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup_form.html', {'form': form})
