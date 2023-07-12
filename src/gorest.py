
"""Python file that fetches user and user details api."""

import requests
import json

api_url = "https://gorest.co.in/public/v2/users"
user_details_api_url = "https://gorest.co.in/public/v2/users/"

def fetch_user_details():
    user_details_list = []
    user_list = (requests.get(url=api_url)).json()
    for user in user_list:
        user_id = user["id"]
        user_details = (requests.get(url = user_details_api_url+str(user_id))).json()
        user_details_list.append(user_details)
    return user_details_list

response = fetch_user_details()
print(response)
