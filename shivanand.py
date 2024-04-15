""" a simple api call """
import requests

BASE_URL = "https://reqres.in/api/users"

def apicall() -> dict:
    response = requests.get(BASE_URL)
    return response.json()



#this is feature branch 