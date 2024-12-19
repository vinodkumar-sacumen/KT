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
def divide_features(a: int, b: int) -> float:
    try:
        if b==0:
            return "Error : Division by zero is not allowed."
        result=a/b
        return f"Result : {result}"
    except ValueError:
        return "Error : Invalid input. Please enter valid number."
