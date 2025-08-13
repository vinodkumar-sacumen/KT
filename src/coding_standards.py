"""Module for learning coding standards."""
import requests


def fetch() -> int:
    """Fetch api data.

    Returns:
        int: Returns the count.
    """
    response = requests.get(url='https://api.nationalize.io/?name=nathaniel',
                            timeout=30)
    result = response.json().get('count')
    return result


def add_two_numbers(num1: int, num2: int) -> int:
    """Add two integers.

    Args:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: Returns the sum of two integers.
    """
    result = num1 + num2
    return result


def subtract(num1: int, num2: int) -> int:
    """Substraction of 2 numbers.

    Args:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: subtracted value.
    """
    return num1-num2 if num1 > num2 else num2-num1
    # added comment