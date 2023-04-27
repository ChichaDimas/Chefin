from django.shortcuts import render
import requests
from chefin.settings import POSTER_POS_API_KEY
import json

def index(request):
    context = {
        'title':'Store',
    }
    return render(request,'store/index.html',context)

def get_menu_categories(api_key):
    url = 'https://joinposter.com/api/menu.getProducts'

                # для категорий так
    # url = 'https://joinposter.com/api/menu.getCategories'

    params = {
        'token': api_key,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('response')
    return []

# def menu(request):
#     categories = get_menu_categories(POSTER_POS_API_KEY)
#
#     json_str = categories.price
#     price_dict = json.loads(json_str)
#     price = price_dict.get('1')
#
#     context = {'categories': categories,
#                "title":'Hellobro',
#                'price':price,
#                }
#     return render(request, 'menu.html', context)


def menu(request):
    categories = get_menu_categories(POSTER_POS_API_KEY)

    prices = [category.get('price', {}).get('1') for category in categories]

    context = {'categories': categories,
               'prices': prices,
               "title": 'Hellobro', }
    return render(request, 'menu.html', context)
