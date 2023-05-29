import os
from django.http import JsonResponse
from chefin.settings import POSTER_POS_API_KEY, POSTER_VENUE_ID
from cloudipsp import Api, Checkout
from django.shortcuts import render,HttpResponseRedirect
from .helpers import *
from .models import *


def menu(request):
    api_key = POSTER_POS_API_KEY
    fill_database(api_key)

    query = request.GET.get('query')
    category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__icontains=category)

    context = {
        'title': 'Store - магазин',
        'products': products,
    }
    return render(request, 'store/menu.html', context)





def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    request.session.setdefault('basket', {})
    basket = request.session['basket']
    basket[product_id] = product.to_json()  # преобразование объекта Product в JSON
    request.session.modified = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



def basket_remove(request, product_id):
    basket = request.session.get('basket', {})
    ids = [item.get('id') for item in basket.values()]

    if product_id in ids:
        del basket[str(product_id)]
        request.session['basket'] = basket
        request.session.modified = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




def profile(request):
    # Получаем текущую корзину из сессии пользователя
    basket = request.session.get('basket', {})
    basket_items = basket.values()



    context = {'title': 'Корзина',
               'baskets': basket_items,
               }
    return render(request,'store/baskets.html',context)


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






# def basket_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     request.session.setdefault('basket', {})
#     basket = request.session['basket']
#     basket[product_id] = product.to_json()  # преобразование объекта Product в JSON
#     basket[product_id]['basket_id'] = product_id  # добавление 'basket_id'
#     request.session.modified = True
#
#     # Обновление количества продуктов в корзине
#     basket_items = request.session['basket'].values()
#     total_quantity = sum(item.get('quantity', 1) for item in basket_items)
#     request.session['total_quantity'] = total_quantity
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
#
# def get_quantity_for_basket(product_id, basket_items):
#     for item in basket_items:
#         if str(item['id']) == str(product_id):
#             return item.get('quantity', 0)
#     return 0
#
#
# def profile(request):
#     # Получаем текущую корзину из сессии пользователя
#     basket = request.session.get('basket', {})
#     basket_items = basket.values()
#
#     context = {'title': 'Корзина',
#                'baskets': basket_items,
#                # 'total_quantity': sum(item['quantity'] for item in basket_items),
#                'total_quantity': sum(item.get('quantity', 0) for item in basket_items),
#
#                }
#
#     # Добавляем общую сумму
#     total_sum = sum(item['price'] * get_quantity_for_basket(item['basket_id'], basket_items) for item in basket_items)
#     context['total_sum'] = total_sum
#
#     return render(request,'store/baskets.html',context)
