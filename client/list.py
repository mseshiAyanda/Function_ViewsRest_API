import requests

endpoint = 'http://127.0.0.1:8004/api/articles/'

get_response = requests.get(endpoint, json={"content": "hello world"})

print(get_response.json())