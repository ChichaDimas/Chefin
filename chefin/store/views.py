import os

from django.shortcuts import render
import requests
from chefin.settings import POSTER_POS_API_KEY, POSTER_VENUE_ID
from cloudipsp import Api, Checkout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from store.cart import Cart
from .models import Product
from django.core.files.base import ContentFile
from urllib.request import urlretrieve

import requests
from urllib.parse import urlparse
from django.shortcuts import render
from .helpers import *



def menu(request):
    api_key = POSTER_POS_API_KEY
    fill_database(api_key)
    categories = Product.objects.all()
    context = {'categories': categories}
    return render(request,'store/menu.html',context)



# def get_menu_categories(api_key):
#     url = 'https://joinposter.com/api/menu.getProducts'
#
#     params = {
#         'token': api_key,
#         'format': 'json'
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json().get('response')
#     return []
#
# def menu(request):
#     categories = get_menu_categories(POSTER_POS_API_KEY)
#
#     context = {
#         'categories': categories,
#         'title': 'Hellobro',
#
#     }
#     return render(request, 'store/menu.html', context)


def add_to_cart(request):
    api = Api(merchant_id=1397120,
              secret_key='Not for tests. Test credentials: https://docs.fondy.eu/docs/page/2/ ')
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "amount": 12000
    }
    url = checkout.url(data).get('checkout_url')
    context = {
        'title':'Store',
        'url': url
    }
    return render(request,'store/add_to_cart.html',context)




def index(request):
    context = {
        'title':'Store',
    }
    return render(request,'store/index.html',context)



