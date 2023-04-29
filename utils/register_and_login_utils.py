import requests


def register_user(username: str, password: str) -> str:
    url = 'http://localhost:5000/users/register'
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/json', 'accept': 'application/xml'}

    response = requests.post(url, json=data, headers=headers)

    # Returns username. None otherwise
    if response.status_code == 200:
        return username
    else:
        return "None"


def login_user(username: str, password: str):
    url = 'http://localhost:5000/users/login'
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/json', 'accept': 'application/xml'}

    requests.post(url, json=data, headers=headers)