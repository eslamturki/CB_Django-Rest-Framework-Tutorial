import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything"


endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={'abc': 123}, json={
    "content": 'Hello'})  # HTTP Request
# print(get_response.text)  # print raw source code as raw text

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict


print(get_response.json())
print(get_response.status_code)
