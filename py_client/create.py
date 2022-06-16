import requests


endpoint = "http://localhost:8000/api/product/"

# get_response = requests.get(endpoint, json={'title': 'New Relase from post'})
data = {

    "title": "this field is done"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
