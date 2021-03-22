from django.shortcuts import render

from products.models import Product
from newsletter.forms import EmailSubscribeForm


def index(request):
    """ View to return the index page """

    products = Product.objects.all()[:6]
    form = EmailSubscribeForm()

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'home/index.html', context)
