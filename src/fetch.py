import requests
from requests import Response
import logging


logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.info(f"Api call {url} successful")
        return data["count"]
    return "wrong url"


fetch("https://api.publicapis.org/entries")


def add(num1, num2):
    try:
        result = num1 + num2
        logging.info(f"Addition success {result}")
        return result
    except TypeError:
        logging.error("Invalid Input")


add(10, 10)
add(10, "hi")


def divide(num1, num2):
    try:
        result = num1 / num2
        logging.info(f"Division success {result}")
        return result
    except ZeroDivisionError:
        logging.error("Invalid Input")


divide(10, 2)
divide(20, 0)
