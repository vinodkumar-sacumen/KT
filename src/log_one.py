import requests
import logging

"""configure logger with default log level and log file"""
logging.basicConfig(filename="loginfos.log", level=logging.DEBUG)

"""creating logger for fetching fetch"""
fetch_logger = logging.getLogger("fetch")
fetch_logger.setLevel(logging.DEBUG)

"""formatter for log messages"""
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

"""file handler for fetching logger"""
fetch_handler = logging.FileHandler("fetched.log")
fetch_handler.setLevel(logging.DEBUG)
fetch_handler.setFormatter(formatter)

"""add fetch handler to fetch logger"""
fetch_logger.addHandler(fetch_handler)


def fetch(url):
    try:
        fetch_logger.debug(f"fetching data {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fetch_logger.debug("data fetched successfully")
        return data

    except requests.exceptions.RequestException as e:
        fetch_logger.error(f"An error occurred : {str(e)}")
        raise RuntimeError(str(e))


result = fetch("https://api.publicapis.org/entries")
