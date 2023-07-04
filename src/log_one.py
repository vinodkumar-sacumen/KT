import requests
import logging


def fetch(url):
    try:
        logging.debug(f"fetching data {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.debug("data fetched successfully")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred : {str(e)}")
        raise RuntimeError(str(e))


print(fetch(url="https://api.publicapis.org/entries"))


fetch("https://api.publicapis.org/entries")
