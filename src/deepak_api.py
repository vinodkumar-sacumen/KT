"""Making an API call"""

import requests

def make_api_call() -> None:
    """Fetch data from API."""
    try:
        response = requests.get(url = 'https://api.publicapis.org/entries')
        if response.status_code == 200:
            print(response.json())
        else:
            print(f'Response status code is {response.status_code}')
    except Exception as e:
        print(f'Error:{e}')
        raise Exception(e)
    
if __name__ == "__main__":
    make_api_call()