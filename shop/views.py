from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from shop.models import *


def index(request):
    event_list = Event.objects.all()
    product_list = Product.objects.all()
    context = {
        'events': event_list,
        'products': product_list
    }
    return render(request, 'shop/registration/index.html', context)

def product_list(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list
    }
    return render(request, 'shop/product/product_list.html', context)