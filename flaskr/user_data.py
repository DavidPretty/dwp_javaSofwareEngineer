import requests

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")

def get_users():
    return requests.get("https://bpdts-test-app.herokuapp.com/users")