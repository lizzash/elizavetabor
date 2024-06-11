import requests
import math
from PIL import Image,ImageDraw
from io import BytesIO

# Задаем список точек (широта, долгота)
points = [
    (54.727646, 55.945091),
    (54.726600, 55.944613),
    (54.728021, 55.935748),
    (54.721175, 55.932290)
]

def calculate_distance(point1, point2):
    # Рассчитываем расстояние между двумя точками с помощью формулы гаверсинусов
    radius_earth = 6371  # Радиус Земли в километрах
    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) * math.sin(delta_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius_earth * c
    return distance

# Определяем длину пути
total_distance = 0
for i in range(len(points) - 1):
    point1 = points[i]
    point2 = points[i + 1]
    distance = calculate_distance(point1, point2)
    total_distance += distance

print(f"Длина пути: {total_distance:.2f} км")

# Отобразим путь на карте с помощью сервиса Yandex Maps
api_key = "01f86158-7ab8-4a36-96b3-aacf7693b5d8"
map_params = {
    'l': 'map',
    'size': '650,450',
    'pt': '~'.join([f'{point[1]},{point[0]},pm2wtl' for point in points]),
    'pl': ','.join([f'{point[1]},{point[0]}' for point in points]),
    'key': api_key
}
map_api_server = "https://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
image = Image.open(BytesIO(response.content))

# Добавляем метку в среднюю точку пути
avg_lat = (points[0][0] + points[-1][0]) / 2
avg_lon = (points[0][1] + points[-1][1]) / 2
marker_size = 10
draw = ImageDraw.Draw(image)
draw.rectangle([avg_lon - marker_size, avg_lat - marker_size, avg_lon + marker_size, avg_lat + marker_size], fill="red")

image.show()