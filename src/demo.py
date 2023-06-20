"""Demo python file."""

import requests
from requests import Response

# PASSWORD = "password123"


def my_func(name: str) -> str:
    """Demo my function.

    Args:
        name (str): name of type string

    Returns:
        str: returns a phrase with the name passed.
    """
    return f"Hello {name}, welcome to Sacumen."

# print(my_func("Python developer"))


def add(num1: int, num2: int) -> int:
    """Sum of 2 numbers.

    Args:
        num1 (int) Optional: a number.
        num2 (int): another number.

    Returns:
        int: result of int which is sum of num1 and num2.
    """
    return num1 + num2


# print(add("hello", 20))


def fetch(url: str) -> Response:
    """Fetch the data from an API.

    Args:
        url (str): Actual url required to fetch data from.
    """
    return requests.get(url, timeout=20)


# print(fetch(url="https://api.publicapis.org/entries"))



def fun():
    return "hello world"

def vinod()-> None:
    """Demo Method"""
    return "Nothing"

def Ashwini():
    return "Hi"