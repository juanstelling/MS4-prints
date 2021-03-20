from django.shortcuts import render, redirect, reverse
from django.contrib import messages




def contact(request):
    """ A view to return the contact page """


    template = 'contact/contact.html'

    return render(request, template)