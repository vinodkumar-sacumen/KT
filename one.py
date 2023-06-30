import pytest, json
import requests
from requests import Response
from tests.mocks import functions


def fetch(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred : {str(e)}")


print(fetch(url="https://api.publicapis.org/entries"))


def fetch_count_one(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        count = data["count"]
        print(f"count={count}")
        count1 = 1425
        if count == count1:
            print(f"count = {count}")
        else:
            print(f"count={count1}")
    except requests.exceptions.RequestException as e1:
        raise RuntimeError(f"An error occurred : {str(e1)}")


fetch_count_one("https://api.publicapis.org/entries")
