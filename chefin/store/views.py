from django.shortcuts import render
import requests
from django.conf import settings
from requests import Response

from chefin.settings import POSTER_POS_API_KEY, POSTER_VENUE_ID
from django.http import JsonResponse, HttpResponseRedirect
import json
from cloudipsp import Api, Checkout



def get_menu_categories(api_key):
    url = 'https://joinposter.com/api/menu.getProducts'

    params = {
        'token': api_key,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('response')
    return []

def menu(request):
    categories = get_menu_categories(POSTER_POS_API_KEY)
    photo = []
    price = []

    for category in categories:
        if category.get('price'):
            price_str = category['price']['1']
            price_float = float(price_str) / 100
            price_formatted = round(price_float, 2)
            price.append(price_formatted)


    for category in categories:
        if category.get('photo'):
            photo.append(f"https://joinposter.com{category['photo']}")

    for i, category in enumerate(categories):
        if category.get('photo'):
            category['photo'] = photo[i]

        if category.get('price'):
            category['price'] = price[i]

    context = {
        'categories': categories,
        'title': 'Hellobro',

    }
    return render(request, 'store/menu.html', context)



def add_to_cart(request):
    api = Api(merchant_id=1397120,
              secret_key='Not for tests. Test credentials: https://docs.fondy.eu/docs/page/2/ ')
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "amount": 300
    }
    url = checkout.url(data).get('checkout_url')
    print(url)
    context = {
        'title':'Store',
        'url': url
    }
    return render(request,'store/add_to_cart.html',context)



# def basket_add(request,product_id):
#     product = menu.request.get(id=product_id)
#     baskets = Basket.objects.filter(user=request.user,product=product)
#
#     if not baskets.exists():
#         Basket.objects.create(user=request.user,product=product,quantity=1)
#     else:
#         basket = baskets.first()
#         basket.quantity+=1
#         basket.save()
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])


def index(request):
    context = {
        'title':'Store',
    }
    return render(request,'store/index.html',context)



def pay(request):

    api = Api(merchant_id=1397120,
          secret_key='Not for tests. Test credentials: https://docs.fondy.eu/docs/page/2/ ')
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "amount": 300
        }
    url = checkout.url(data).get('checkout_url')
    print(url)
    context = {
        'url': url
    }
    return render(request, 'store/payment.html', context)


