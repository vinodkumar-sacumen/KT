"""Fetch python file."""

import logging

import requests

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch(url: str) -> str:
    """Passing Url.

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


def add(num1, num2):
    """Sum of two number

    Args:
        num1 (int): a number.
        num2 (int): another number.

    Returns:
        int:result of int which is sum of num1 and num2.
    """
    try:
        result = num1 + num2
        logging.info("Addition success %s ", result)
        return result
    except TypeError:
        logging.error("Invalid Input")
    return None


add(10, 10)
add(10, "hi")


def divide(num1, num2):
    """Division of two number.

    Args:
        num1 (int): a number.
        num2 (int): another number.

    Returns:
        int: result of int which is sum of num1 and num2.
    """
    try:
        result = num1 / num2
        logging.info("Division success %s ", result)
        return f"result is {result}"
    except ZeroDivisionError:
        logging.error("Invalid Input")
    return None


divide(10, 2)
divide(20, 0)
