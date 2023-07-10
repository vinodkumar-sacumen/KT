import requests


def fetch(url): 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(str(e))


fetch("https://api.publicapis.org/entries")


def fetch_count_one(url):
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            count = data["count"]
            count1 = 1425
            if count == count1:
                print(f"count = {count}")
            else:
                print(f"count={count1}")
        else:
            raise RuntimeError(f"requests failed{response.status_code}")
    except requests.exceptions.RequestException as e1:
        raise RuntimeError(f"An error occurred : {str(e1)}")


fetch_count_one("https://api.publicapis.org/entries")