import requests

# Получаем список городов от пользователя
cities = input("Введите города (через запятую): ").split(',')

# Переменные для хранения самого южного города и его широты
southernmost_latitude = 90
southernmost_city = ""

# API ключ для Yandex Search API
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

# Перебираем список введенных городов
for city in cities:
    city = city.strip()  # Удаляем возможные пробелы в начале и конце названия города
    if city == "":
        continue
    try:
        # Формируем запрос к Yandex Search API, чтобы получить данные о городе
        response = requests.get("https://search-maps.yandex.ru/v1/", params={"apikey": api_key, "text": city, "lang": "ru_RU", "type": "geo"})
        data = response.json()

        # Извлекаем координаты города
        point = data['features'][0]['geometry']['coordinates']
        latitude = point[1]

        # Если координата южнее текущей самой южной, обновляем самый южный город
        if latitude < southernmost_latitude:
            southernmost_latitude = latitude
            southernmost_city = city

    except:
        print(f"Не удалось найти координаты для города {city}.")

# Выводим название самого южного города
if southernmost_city:
    print(f"Самый южный город: {southernmost_city}")
else:
    print("Не введен город")
