"""Script that fetchs all api data"""
import requests

def fetch():
    response = requests.get(url = 'https://api.nationalize.io/?name=nathaniel')
    result = response.json().get('count')
    return result

count = fetch()
print(count)

def add_two_numbers(num1,num2):
    '''
    Adds two numbers
     
    '''
    result = num1 + num2 
    return result

sum_value = add_two_numbers(20,20)
print(sum_value)