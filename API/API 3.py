
import requests
from PIL import Image
from io import BytesIO

# получаем координаты от пользователя
latitude = input("Введите широту: ")
longitude = input("Введите долготу: ")

# формируем параметры для запроса к StaticMapsAPI
address_ll = "{0},{1}".format(latitude, longitude)
delta = "0.005"  # размеры
map_params = {
    "ll": address_ll,  # центрируем карту на введенных координатах
    "spn": ",".join([delta, delta]),
    "l": "sat"  # указываем тип карты (спутниковая карта)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# Выполняем запрос
response = requests.get(map_api_server, params=map_params)
# читаем изображение из содержимого ответа
image = Image.open(BytesIO(response.content))

# отображаем изображение
image.show()
