import requests
import logging

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch(url):
    response = requests.get(url)    # fetch("https://api.publicapis.org/entries")
    if response.status_code == 200:
        data = response.json()
        logging.info(f"Api call {url} successful")
        return data["count"]
    return "wrong url"

def multiply(a: int, b: int) -> int:
    """multiply 2 nos.
    Args:
        a (int): num1
        b (int): num2
    Returns:
        int: returns an int that is multipied.
    """
    return a * b

# TODO: Add your code here..
def divide_features(a: int, b: int) -> float:
    try:
        if b==0:
            return "Error : Division by zero is not allowed."
        result=a/b
        return f"Result : {result}"
    except ValueError:
        return "Error : Invalid input. Please enter valid number."

def find_difference(num1: int, num2: int) -> int:
    """Finding the difference of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: returnn difference of first and second number
    """
    if (type(num1) == int) and (type(num2) == int ):
        return (num1-num2) if (num1 > num2) else (num2-num1)
    else:
        return "Given input is not as expected"