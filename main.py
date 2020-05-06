# Key for geocoder API: 40d1649f-0493-4b70-98ba-98533de7710b
# Key for search API: dda3ddba-c9ea-4ead-9010-f43fbc15c6e3

import sys
import requests
from io import BytesIO
from PIL import Image
from scale import scope

address = " ".join(list(map(str.strip, sys.stdin)))

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

map_params = {
    "ll": ",".join([geo_obj_longitude, geo_obj_latitude]),
    "spn": ",".join([str(delta_x), str(delta_y)]),
    "pt": ",".join([geo_obj_longitude, geo_obj_latitude, "pm2rdm1"]),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()