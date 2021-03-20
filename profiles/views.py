from django.shortcuts import render


def profile(request):
    """ Shows the profile of user. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
