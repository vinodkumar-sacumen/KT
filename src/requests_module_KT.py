"""Script that fetchs all api data"""
import requests

def fetch():
    response = requests.get(url = 'https://api.nationalize.io/?name=nathaniel')
    result = response.json().get('count')
    return result

count = fetch()
print(count)
