import requests

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

geo_obj_coordinates = geo_obj["Point"]["pos"].split()

# Определяем район

district_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": ",".join(geo_obj_coordinates),
    "kind": "district",
    "format": "json"
}

district_response = requests.get(geo_api_server, params=district_params)

json_district_response = district_response.json()
district = json_district_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]

print(district)