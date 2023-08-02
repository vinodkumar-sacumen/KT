import requests

def return_count():
    '''
    Makes an api call and returns the count 
    '''
    response = requests.get(url = 'https://api.nationalize.io/?name=nathaniel')
    result = response.json().get('count')
    return result

count = return_count()
print(count)
