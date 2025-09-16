from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'single_product.html', {"product": product})
