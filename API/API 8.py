import math

# Функция, считающая расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance

# Получаем адреса от пользователя
home_address = input("Введите адрес вашего дома: ")
university_address = input("Введите адрес вашего университета: ")

# Преобразуем адреса в координаты
home_coordinates = tuple(map(float, input("Введите координаты вашего дома (долгота, широта): ").split(', ')))
university_coordinates = tuple(map(float, input("Введите координаты вашего университета (долгота, широта): ").split(', ')))

# Вычисляем расстояние между домом и университетом
distance = lonlat_distance(home_coordinates, university_coordinates)

# Выводим результат
print(f"Расстояние между домом ({home_address}) и университетом ({university_address}) составляет {distance}")