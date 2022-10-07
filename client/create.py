import requests

endpoint = 'http://127.0.0.1:8004/api/articles/'

data = {
    "tittle": "This firld is required",
    "author": "Mseshi Mndayi"
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())