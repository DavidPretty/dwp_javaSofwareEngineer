import requests
from math import radians, sin, cos, sqrt, asin
from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(get_londoners().json())

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")

def get_users():
    return requests.get("https://bpdts-test-app.herokuapp.com/users")

def get_haversine(latX, lonX, latY, lonY):
    R = 3958.8  # Earth's radius in miles

    diffLat = radians(latY - latX)
    diffLon = radians(lonY - lonX)
    latX = radians(latX)
    latY = radians(latY)

    a = sin(diffLat / 2)**2 + cos(latX) * cos(latY) * sin(diffLon / 2)**2
    c = 2 * asin(sqrt(a))

    return R * c
