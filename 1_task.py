import requests
import json

city_name = 'Omsk'
API_KEY = '99543fcf83dd955d992925d2271174a8'

def get_coord(city_name):
    geocoding_URL = (f'http://api.openweathermap.org/geo/1.0/'
                     +f'direct?q={city_name}&limit=1&appid={API_KEY}')
    response = requests.get(geocoding_URL)
    inf = json.loads(response.text)[0]
    return inf['lat'], inf['lon']

def get_data(lat, lon):
    geocoding_URL = (f'https://api.openweathermap.org/data/2.5/'
                   +f'weather?lat={lat}&lon={lon}&appid={API_KEY}')
    response = requests.get(geocoding_URL).json()

    return response

def present_data(data):
    print(f'Погода: {data['weather'][0]['description']}')
    print(f'Температура: {data['main']['temp'] - 273}')
    print(f'Влажность: {data['main']['humidity']}')
    print(f'Давление: {data['main']['pressure']}')

lat, lon = get_coord(city_name)
data = get_data(lat, lon)
present_data(data)


