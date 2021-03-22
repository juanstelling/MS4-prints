from django.shortcuts import render


def company(request):
    """ A view to return the company page """

    return render(request, 'pages/company.html')


def sustainability(request):
    """ A view to return the sustainability page """

    return render(request, 'pages/sustainability.html')


def faq(request):
    """ A view to return the FAQ page """

    return render(request, 'pages/faq.html')


def return_policy(request):
    """ A view to return the return policy page """

    return render(request, 'pages/return_policy.html')