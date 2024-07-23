from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from marketplace.models import Product
# Create your views here.


class HomeView(TemplateView):
    template_name = 'marketplace/index.html'

class StoreView(ListView):
    model = Product
    template_name = 'marketplace/store.html'
    context_object_name = 'available_product'

    def get_queryset(self):
        # Filter to show only active Product
        return Product.objects.filter(is_available=True)