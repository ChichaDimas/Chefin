import requests
from django.core.files.base import ContentFile
from .models import Product
import os
from pprint import pprint


def get_menu_categories(api_key):
    url = 'https://joinposter.com/api/menu.getProducts'

    params = {
        'token': api_key,
        'format': 'json'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json().get('response', [])


def fill_database(api_key):
    url = 'https://joinposter.com/api/menu.getProducts'

    params = {
        'token': api_key,
        'format': 'json'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return

    if response.status_code == 200:
        # Delete existing categories
        Product.objects.all().delete()

        categories = get_menu_categories(api_key)

        for category in categories:
            # Create new categories

            # Create new products
            try:
                price = list(category.get('price', {}).values())[0]
                price_for_view = f"{price[:-2]}.{price[-2:]}"
                product, created = Product.objects.get_or_create(
                    name=category.get('product_name'),
                    category=category.get('category_name'),
                    description=category.get('product_production_description'),
                    price=price,
                    price_for_view=price_for_view,
                    image=f"https://joinposter.com{category.get('photo', '')}",
                )
            except Exception as err:
                print(f"Error: {err}")
                continue

        # categories_data = response.json().get('response')
        #
        #
        # for category_data in categories_data:
        #     products_data = category_data.get('products', [])
        #     if products_data:
        #         category, _ = ProductCategory.objects.get_or_create(
        #             name=category_data.get('product_name'),
        #             defaults={'description': category_data.get('product_production_description')}
        #         )
        #         for product_data in products_data:
        #             name = product_data.get('product_name', '')
        #             description = product_data.get('product_production_description', '')
        #             price_cents = product_data.get('price', {}).get('1', 0)
        #             price = price_cents / 100
        #
        #             image_url = f"https://joinposter.com{product_data.get('photo', '')}"
        #             image_name = image_url.split('/')[-1]
        #             image_content = ContentFile(requests.get(image_url).content)
        #
        #             try:
        #                 product_image = Product.objects.create(image=image_content, name=image_name, category=category)
        #                 product = Product.objects.create(name=name, description=description, price=price, image=product_image)
        #             except Exception as e:
        #                 print(f"Failed to create product {name}: {str(e)}")
