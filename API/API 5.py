import requests
from PIL import Image
from io import BytesIO

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll=input("Ведите адрес: ")

search_params = {
    "apikey": api_key,
    "text": address_ll,
    "lang": "ru_RU",
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()
coords=json_response['features'][0]['geometry']['coordinates']
address_ll = "{0},{1}".format(coords[0], coords[1])

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
nearest_pharmacy = json_response["features"][0]
# Название организации.
pharmacy_name = nearest_pharmacy["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
pharmacy_address = nearest_pharmacy["properties"]["CompanyMetaData"]["address"]

# Получаем координаты ответа.
coords = nearest_pharmacy["geometry"]["coordinates"]
pharmacy_coords = "{0},{1}".format(coords[0], coords[1])

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": address_ll,
    "l": "map",
    "pt": "{0},pm2dgl".format(pharmacy_coords)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

# Read the image from the response content
image = Image.open(BytesIO(response.content))

# Show the image
image.show()
