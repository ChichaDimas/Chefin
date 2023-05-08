"""
URL configuration for chefin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from store.views import *

# from chefin.store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('profile/', profile, name='profile'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_remove/<int:product_id>/', basket_remove, name='basket_remove'),


    # path('baskets/remove/<int:product_id>/', basket_remove, name='basket_remove'),

    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]


    # path('payment/', payment, name='payment'),
