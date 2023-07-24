
"""Python file that fetches user and user details api."""

import requests
import json

api_url = "https://gorest.co.in/public/v2/users"
user_details_api_url = "https://gorest.co.in/public/v2/users/"

def fetch(api_url,user_details_api_url):
    user_id_list = user_list(api_url)
    if user_id_list:
        user_details_list = user_details(user_details_api_url,user_id_list)
        return user_details_list
    else:
        return user_id_list

def user_list(url):
    user_id_list = []
    user_list = requests.get(url=url)
    if user_list.status_code == 200:
        user_list = user_list.json()
    else:
        return user_id_list
    for user in user_list:
        user_id_list.append(user["id"])
    return user_id_list

def user_details(url,user_id_list):
    user_details_list = []
    for user_id in user_id_list:
        response = requests.get(url = url+str(user_id))
        if response.status_code == 200:
            user_details_list.append(response.json())
        else:
            user_details_list
    return user_details_list

response = fetch(api_url,user_details_api_url)
print(response)
