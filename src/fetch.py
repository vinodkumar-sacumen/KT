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

# TODO: Add your code here..
def add(num1:int,num2:int)->int:
    """get_sum_of_two_nums

    Args:
        int (num1): First number
        int (num2): Second number

    Returns:
        int: Returns the sum of num1 and num2
    """

    return num1+num2
