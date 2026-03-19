import requests
import json

def get_info(id):
    geocoding_URL = (f'https://rickandmortyapi.com/api/character/{id}')
    response = requests.get(geocoding_URL)
    return response.json()


def present_data(data):
    print(f'name: {data['name']}')
    print(f'status: {data['status']}')
    print(f'gender: {data['gender']}')
    print(f'species: {data['species']}')
    print(f'location: {data['location']['name']}')



for id in range(6,10):
    data = get_info(id)
    present_data(data)
    print('--------------')




