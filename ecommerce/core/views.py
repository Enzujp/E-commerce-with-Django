from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()[0:6]

    return render(request, 'core/index.html', {
        'products': products
    })


def about(request):
    return render(request, 'core/about.html')