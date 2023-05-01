from django.shortcuts import render
import requests
from django.conf import settings
from chefin.settings import POSTER_POS_API_KEY, POSTER_VENUE_ID

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

def payment(request):


    url = 'https://joinposter.com/api/incomingOrders.createIncomingOrder?token=590085:2678523168eeca3ec11d86a373e60ef2'

    incoming_order = {
        'spot_id': 1,
        'phone': '+380680000000',
        'products': [
            {
                'product_id': 6,
                'count': 1
            }
        ]
    }


    amount = 1000 # сумма оплаты в копейках (в данном случае 10 рублей)
    data = {
        'venue_id': settings.POSTER_VENUE_ID,
        'amount': amount,
    }
    headers = {'Authorization': 'Bearer {}'.format(settings.POSTER_POS_API_KEY)}

    # отправляем запрос на создание оплаты
    response = requests.post('https://joinposter.com/api/payments.createPayment', json=data, headers=headers)

    if response.status_code == 200:
        # получаем данные об оплате
        payment_data = response.json()
        # отображаем страницу с данными об оплате для пользователя
        return render(request, 'store/payment.html', {'payment_data': payment_data})
    else:
        # обработка ошибки при создании оплаты
        return render(request, 'store/error.html', {'error': 'Ошибка при создании оплаты'})


# url = 'https://joinposter.com/api/incomingOrders.createIncomingOrder?token=590085:2678523168eeca3ec11d86a373e60ef2'
#
# incoming_order = {
#     'spot_id': 1,
#     'phone': '+380680000000',
#     'products': [
#         {
#             'product_id': 8,
#             'count': 1
#         }
#     ]
# }
#
# headers = {'Content-Type': 'application/json'}
#
# response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
#
# print(response.text)


from django.http import JsonResponse


def pay(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        amount = request.POST.get('amount')
        order_id = request.POST.get('order-id')
        venue_id = 1  # ID места на Poster

        # Отправляем запрос на оплату
        url = 'https://joinposter.com/api/incomingOrders.createIncomingOrder?token=590085:2678523168eeca3ec11d86a373e60ef2'
        data = {
            'amount': amount,
            'order_id': order_id,
            'venue_id': venue_id
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)

        # Возвращаем результат в виде JSON
        return JsonResponse({'success': True})

def add_to_cart(request):
    context = {
        'title':'Store',
    }
    return render(request,'store/add_to_cart.html',context)