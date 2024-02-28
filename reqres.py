import requests
from json import loads, dumps

URL = "https://reqres.in/api/users"

payload = {}
headers = {}

def get(URL):
    users_data = requests.get(URL)
    print(users_data.text)
    print("Status: ", users_data.status_code)
    return users_data
get(URL)

user = {
    "nombre": "Ignacio",
    "trabajo": "Profesor"
}

def post(user: dict):
    headers = {'Content-Type': 'application/json'}
    created_user = requests.post(url=URL, headers = headers, data = dumps(user))
    print(created_user.text)
    print("Status: ", created_user.status_code)
    return  created_user

post(user)

user1 = {
    "nombre": "Morpheus",
    "Residence": "Zion"
}

def put(user1:dict):
    url = URL + "/2"
    headers = {'Content-Type': 'application/json'}
    updated_user = requests.put(url, headers = headers, data = dumps(user1))
    print(updated_user.text)
    print("Status: ", updated_user.status_code)
    return updated_user

put(user1)

user2 = {"nombre": "Tracey"}

def delete(user2:dict):
    delete_user = requests.delete(url=URL, headers = headers, data = payload)
    print(delete_user.text)
    print("Status: ", delete_user.status_code)
    return delete_user

delete(user2)