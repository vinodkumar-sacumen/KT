"""Script that fetchs all api data"""
import requests

def fetch():
    response = requests.get(url = 'https://api.nationalize.io/?name=nathaniel')
    result = response.json().get('count')
    return result

def add_two_numbers(num1,num2):
    '''
    Adds two numbers
    '''
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
