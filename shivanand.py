""" set of tasks """
import requests

BASE_URL = "https://reqres.in/api/users"

def apicall() -> dict:
    response = requests.get(BASE_URL)
    return response.json()

def sub(num1: int, num2: int) -> int:
    """Substraction of 2 numbers.
    Args:
        num1 (int): first integer. should be greater than num2.
        num2 (int): second integer. Should be less than num1.

    Returns:
        int: returns difference value of num1 and num2.
    """
    sub = num1 - num2
    return sub


class TASK2:
    def add_no(self, num1:int, num2:int) ->int:
        """Addition of 2 numbers.
    Args:
        num1 (int): first number.
        num2 (int): second number.
    Returns:
        int: returns sum of num1 and num2
    """
        return num1+num2

    
