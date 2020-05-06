import sys
import requests
from io import BytesIO
from PIL import Image
from scale import scope
from dist import distance

address = input()

# Получаем координаты заданного объекта

geo_api_server = "http://geocode-maps.yandex.ru/1.x/"

geo_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": address,
    "format": "json"
}

response = requests.get(geo_api_server, params=geo_params)
json_response = response.json()

geo_obj = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

geo_obj_coordinates = geo_obj["Point"]["pos"]
geo_obj_longitude, geo_obj_latitude = geo_obj_coordinates.split(" ")

delta_x, delta_y = scope(geo_obj)

objects1 = [geo_obj_longitude, geo_obj_latitude, "pm2rdm1"]

# Получаем координаты ближайшей аптеки

search_api_server = "http://search-maps.yandex.ru/v1/"

search_params = {
    "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
    "text": "Аптеки",
    "ll": f"{geo_obj_longitude},{geo_obj_latitude}",
    "lang": "ru_RU"
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()

objects2 = []

for i in range(10):
    pharmacy_longitude = json_response["features"][i]["geometry"]["coordinates"][0]
    pharmacy_latitude = json_response["features"][i]["geometry"]["coordinates"][1]

    objects2 += [pharmacy_longitude, pharmacy_latitude, f"pm2rdm{i}"]

# Формируем итоговый запрос

objects = list(map(str, objects1 + objects2))

map_params = {
    "ll": ",".join([geo_obj_longitude, geo_obj_latitude]),
    "spn": ",".join([str(delta_x), str(delta_y)]),
    "pt": ",".join(objects),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

object_coordinates = (float(geo_obj_longitude), float(geo_obj_latitude))

for i in range(10):
    pharmacy_coordinates = (objects2[i * 3], float(objects[i * 3 + 1]))
    print(pharmacy_coordinates)

    _distance = round(distance(object_coordinates, pharmacy_coordinates) / 1000, 2)

    print(f"Расстояние между вашим расположением и аптекой номер {i + 1} составляет {_distance} километров")

Image.open(BytesIO(response.content)).show()
