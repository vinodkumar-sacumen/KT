"""Fetch python file."""

import logging
from requests import Response
import requests

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch(url: str) -> Response:
    """Pass Url to the fetch method.

    Args:
        url (str): a string.

    Returns:
        str:Fetching data from given API.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        logging.info("Api call successful for %s", url)
        return data["count"]
    return "wrong url"


fetch("https://api.publicapis.org/entries")


def add(num1: int, num2: int) -> int:
    """Sum of two integer number.

    Args:
        num1 (int): a number.
        num2 (int): another number.

    Returns:
        int: result of num1 and num2 which is int.
    """
    result = num1 + num2
    logging.info("Addition success %s ", result)
    logging.error("Invalid Input")
    return result


add(10, 10)


def divide(num1: int, num2: int) -> int:
    """Division of two number.

    Args:
        num1 (int): a number.
        num2 (int): another number.

    Returns:
        int: result of num1 and num2 which is int.
    """
    result = num1 // num2
    logging.info("Division success %s ", result)
    logging.error("Invalid Input")
    return result


divide(10, 2)
