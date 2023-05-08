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

    context = {'title': 'Store - магазин',
        'products': Product.objects.all(),
        }
    return render(request,'store/menu.html',context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    request.session.setdefault('basket', {})
    basket = request.session['basket']
    basket[product_id] = product.to_json()  # преобразование объекта Product в JSON
    request.session.modified = True
    # return JsonResponse({'success': True})
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

# def profile(request):
#     # Получаем текущую корзину из сессии пользователя
#     basket = request.session.get('basket', {})
#     print(basket)
#     basket_items = basket.keys()  # получаем ключи из словаря basket
#
#     # basket_items = basket.values()
#
#     ids = [item.get('id') for item in basket.values()]
#     context = {'title': 'Корзина',
#                'baskets': basket,
#                'product_ids': ids,
#                }
#
#     # print(ids)
#     return render(request,'store/baskets.html',context)




def basket_remove(request, product_id):
    basket = request.session.get('basket', {})
    ids = [item.get('id') for item in basket.values()]

    if product_id in ids:
        del basket[str(product_id)]
        request.session['basket'] = basket
        request.session.modified = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])





# def basket_remove(request, product_id):
#     basket = request.session.get('basket', {})
#     if product_id in basket:
#         del basket[product_id]
#         request.session['basket'] = basket
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])






# def basket_remove(request,basket_id):
#     basket = Basket.objects.get(id=basket_id)
#     basket.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])



def profile(request):
    # Получаем текущую корзину из сессии пользователя
    basket = request.session.get('basket', {})
    basket_items = basket.values()
    basket_items2 = basket.keys()
    # print(basket_items)

    # total_sum = sum(int(item['price']) * int(item.get('quantity', 1)) for item in basket_items)

    # total_sum = sum(item['price'] * item['quantity'] for item in basket_items)

    # total_quantity = sum(basket.quantity for basket in basket_items )
    context = {'title': 'Корзина',
               'baskets': basket_items,
               'baskets2': basket_items2,
               # 'total_sum':total_sum,
               # 'total_quantity':total_quantity,
               }
    return render(request,'store/baskets.html',context)







# def basket_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     baskets = Basket.objects.filter(customer_id=request.session.session_key, product=product)
#
#     if not baskets.exists():
#         Basket.objects.create(customer_id=request.session.session_key, product=product, quantity=1)
#     else:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])





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






