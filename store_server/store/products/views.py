from django.shortcuts import render

from products.models import Product, ProductCategory, Basket
from users.models import User
# Create your views here.


def index(request):
    context = {'title': 'Bib Bob'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product).firts()

    if not basket:
        Basket.objects.create.create(user=request.user, product=product, quantity=1)
    else:
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META('HTTP_REFERER'))
