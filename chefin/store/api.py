#
# from chefin.settings import POSTER_POS_API_KEY
# import requests
#
# def get_menu_items():
#     url = 'https://joinposter.com/api/menu.getCategories'
#     params = {
#         'token': POSTER_POS_API_KEY,
#         'format': 'json'
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json().get('response')
#     return []
#
