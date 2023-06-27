import pytest
import requests, pytest_mock, pytest_vcr
from requests import Response
from tests.mocks import functions


def fetch(url):
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
    return response


print(fetch(url="https://api.publicapis.org/entries"))


def fetch(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    count = data["count"]
    count1 = 1425
    if count == count1:
        print(f"count = {count}")
    else:
        print(f"count={count1}")


fetch("https://api.publicapis.org/entries")
