"""Api Call to entries"""
import requests

def fetch_entries(url: str) -> None :

    """Fetch the response from Api.

    Args:
        url (str): Url to fetch entires from publicapis.
    """
    try:
        response = requests.get(url = url)
        if response.status_code == 200:
            result = response.json()
            print(result)
                  
        else:
            print("Request not proper")
            
    except Exception as e:
        print(f'Error:{e}')
        raise Exception(e)
    
if __name__ == "__main__":
    url="https://api.publicapis.org/entries"
    fetch_entries(url)
