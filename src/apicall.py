""""Requesting the API."""

import requests


def req_api(url: str) -> None:
    """Requesting the API to get the information.

    Args:
        url (str): This is the URL to call the API
    """
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
    except Exception as err:
        print(f"raised err is : {err}")


url = "https://api.publicapis.org/entries"
req_api(url)

