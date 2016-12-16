from django.shortcuts import render

# Create your views here.


def products(request):
    title = 'San Pham'
    context = {'title': title}
    template = 'product.html'
    return render(request, template, context)
