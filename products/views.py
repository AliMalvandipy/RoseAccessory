from django.shortcuts import render
from django.views import generic

from .models import Product
class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


