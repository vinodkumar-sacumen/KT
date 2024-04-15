import requests

BASE_URL = "https://reqres.in/api/users"

def apiCall():
    response = requests.get(BASE_URL)
    print(response.json())

apiCall()