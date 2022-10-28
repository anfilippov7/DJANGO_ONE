from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name').all()
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price').all()
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price').all()
    else:
        phone_objects = Phone.objects.all()
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    phone = [phone for phone in phone_object][0]
    context = {
        'phone': phone,
    }
    return render(request, template, context)



