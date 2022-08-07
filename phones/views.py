from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    name = request.GET.get('name')
    if sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    if sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    if name:
        phones = Phone.objects.all().order_by('name')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.all().filter(slug=slug)
    context = {'product': product}
    return render(request, template, context)