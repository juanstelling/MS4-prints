from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ View that renders the shopping bag page  """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shoppingbag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Succesfully updated "{product.name}" to bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Succesfully added "{product.name}" to bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
