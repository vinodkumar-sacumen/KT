# import pdb


# def greet(a):
#     for i in range(a):
#         print("Good Morning", i + 1)


# """debug start"""
# pdb.set_trace()
# greet(5)

import requests
from requests import Response


def fetch(url):
    response = requests.get(url)
    print(response.status_code)
    # print(type(response))
    # print(response.headers)
    # print(response.content)
    return response


print(fetch(url="https://api.publicapis.org/entries"))


# def fetch(url):
#     return requests.get(url)
