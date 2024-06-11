import sys
import requests

if len(sys.argv) == 1:
    address = input("Введите адрес: ")
else:
    address = ' '.join(sys.argv[1:])
    print(f"Адрес: {address}")

if address:
    # Отправляем запрос к API геокодера и получаем координаты адреса
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    geocode_params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocode_url, params=geocode_params)
    json_response = response.json()
    point = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, point.split())

    # Отправляем запрос к API геокодера и получаем район по координатам
    reverse_geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    reverse_geocode_params = {
        "apikey": api_key,
        "geocode": f"{lon},{lat}",
        "kind": "district",
        "format": "json"
    }
    response = requests.get(reverse_geocode_url, params=reverse_geocode_params)
    json_response = response.json()
    try:
        district = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
        print(f"Адрес находится в районе {district}")
    except IndexError:
        print("Не удалось определить район для данного адреса.")
else:
    print("Адрес не был введен.")
