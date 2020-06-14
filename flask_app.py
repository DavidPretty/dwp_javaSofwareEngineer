import requests

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(get_londoners().json())

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")

def get_haversine():
    pass
