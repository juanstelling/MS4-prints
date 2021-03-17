from django.shortcuts import render
from .models import Product


def all_products(request):
    """ View to return the product page, with sorting and searching queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
