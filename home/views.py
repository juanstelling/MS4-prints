from django.shortcuts import render
from newsletter.forms import EmailSubscribeForm


def index(request):
    """ View to return the index page """

    form = EmailSubscribeForm()

    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)
