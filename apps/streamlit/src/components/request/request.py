import requests

flask_base_url = "http://flask:3001"


def call_flask_api(endpoint):
    response = requests.get(flask_base_url + endpoint)
    return response.json()
