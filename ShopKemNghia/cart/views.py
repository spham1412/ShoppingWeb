from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def cart(request):
    title = 'Gio Hang'
    context = {'title': title}
    template = 'cart.html'
    return render(request, template, context)
