import requests
import logging


def fetch(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        
        
    except requests.exceptions.RequestException as e:
        
        """log error message"""
        
        logging.error(f"failed request : {str(e)}")
        raise RuntimeError(str(e))


"""logging configuration"""

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

fetch("https://api.publicapis.org/entries")
