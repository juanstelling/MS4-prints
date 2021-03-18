from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empy!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IRCnqK3zhNmJSyO2dBAtpYh8HJEf5PJsWJIn8q4qnKCnwYjlsLZgnte2a6fPA3p98oKbFGlitn3ukM5tCrlwI3S00wKEetUvF',
        'client_secret': 'test',
    }

    return render(request, template, context)
