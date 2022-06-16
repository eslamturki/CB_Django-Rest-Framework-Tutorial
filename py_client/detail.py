import requests


endpoint = "http://localhost:9000/api/product/1"

# get_response = requests.get(endpoint, json={'title': 'New Relase from post'})

get_response = requests.get(endpoint)
print(get_response.json())
