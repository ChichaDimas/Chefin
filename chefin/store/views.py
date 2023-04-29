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
    print(type(price[0]))
    print(price)

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
    return render(request, 'menu.html', context)


