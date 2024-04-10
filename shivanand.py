import requests

BASE_URL = 'https://reqres.in/api/users'

response = requests.get(BASE_URL)

# print(response.json())
d = response.json()

# print(d)

for i in d:
    if i == 'data':
        for j in d['data']:
            for k in j :
                print(f" {k } --->  {j[k]}") 
            print()