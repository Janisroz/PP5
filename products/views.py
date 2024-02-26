# pylint: disable=import-error
from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Returns All Products Page and handles sorting and searching
    """

    products = Product.objects.all()

    context = {
        'products' : products
    }

    return render(request, 'products/products.html', context)
