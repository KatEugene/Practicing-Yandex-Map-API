import math
import requests

static_map_server = "https://static-maps.yandex.ru/1.x/"
geo_code_server = "https://geocode-maps.yandex.ru/1.x/"
search_server = "http://search-maps.yandex.ru/v1/"

geo_api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
search_api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


def distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    result = math.sqrt(dx * dx + dy * dy)

    return result


def scale(envelope):
    lower_corner = list(map(float, envelope["lowerCorner"].split()))
    upper_corner = list(map(float, envelope["upperCorner"].split()))

    _delta_x = (upper_corner[0] - lower_corner[0]) * 0.5
    _delta_y = (upper_corner[1] - lower_corner[1]) * 0.5

    return _delta_x, _delta_y


def get_object_coordinates(address):
    geo_code_params = {
        "apikey": geo_api_key,
        "geocode": address,
        "format": "json"
    }

    geo_code_response = requests.get(geo_code_server, params=geo_code_params)
    geo_code_json_response = geo_code_response.json()

    geo_obj = geo_code_json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    geo_obj_coordinates = geo_obj["Point"]["pos"]

    return list(map(float, geo_obj_coordinates.split()))


def get_object_scope(address):
    geo_code_params = {
        "apikey": geo_api_key,
        "geocode": address,
        "format": "json"
    }

    geo_code_response = requests.get(geo_code_server, params=geo_code_params)
    geo_code_json_response = geo_code_response.json()

    geo_obj = geo_code_json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    envelope = geo_obj["boundedBy"]["Envelope"]

    return scale(envelope)


def get_object_on_map(object_coordinates, kind, delta_x=None, delta_y=None, z=None, pt=None):
    static_map_params = {
        "ll": object_coordinates,
        "l": kind
    }
    if delta_x and delta_y:
        static_map_params["spn"] = f"{delta_x},{delta_y}"
    else:
        static_map_params["z"] = z
    if pt:
        static_map_params["pt"] = pt
    print(static_map_params)
    static_map_response = requests.get(static_map_server, params=static_map_params)
    return static_map_response.content


def kind_of_object(address):
    geo_code_params = {
        "apikey": geo_api_key,
        "geocode": address,
        "format": "json"
    }

    geo_code_response = requests.get(geo_code_server, params=geo_code_params)
    geo_code_json_response = geo_code_response.json()

    geo_obj = geo_code_json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    return geo_obj["metaDataProperty"]["GeocoderMetaData"]["kind"]
