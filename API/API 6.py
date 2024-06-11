import requests
import random
from PIL import Image
from io import BytesIO
#список городов, которые будут использоваться в игре:
CITIES = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород", "Казань", "Челябинск", "Омск",
          "Самара", "Ростов-на-Дону"]

geocode_url = "https://geocode-maps.yandex.ru/1.x/"
map_url = "https://static-maps.yandex.ru/1.x/"

api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

while True:
    #Для получения случайного города из списка, для выбора случайного типа карты/спутника из списка ["map", "sat"]
    city = random.choice(CITIES)
    map_type = random.choice(["map", "sat"])

    geocode_params = {
        "apikey": api_key,
        "geocode": city,
        "format": "json"
    }
    response = requests.get(geocode_url, params=geocode_params)
    json_response = response.json()
    point = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, point.split())

    map_params = {
        "ll": f"{lon},{lat}",
        "z": "13",
        "l": map_type,
        "size": "450,450"
    }
    map_response = requests.get(map_url, params=map_params)

    img = Image.open(BytesIO(map_response.content))
    img.show()

    input_city = input("Угадайте город: ")
    if input_city.lower() == city.lower():
        print("Угадали!")
    else:
        print(f"Неправильно. Это был город {city}.")

    play_again = input("Сыграть еще раз? (y/n) ")
    if play_again.lower() == "n":
        break
