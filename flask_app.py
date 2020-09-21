import requests
from math import radians, sin, cos, sqrt, asin
from flask import Flask, jsonify
from geo import LONDON_LAT, LONDON_LONG, NEARBY, R

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(get_londoners_and_nearby())

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")

def get_users():
    return requests.get("https://bpdts-test-app.herokuapp.com/users")

def get_nearby():
    users = get_users().json()
    nearby = []
    for user in users:
        if get_haversine(float(user["latitude"]), float(user["longitude"]), \
        LONDON_LAT, LONDON_LONG) <= NEARBY:
            nearby.append(user)
    return nearby

def get_londoners_and_nearby():
    londoners = get_londoners().json()
    nearby = get_nearby()
    londoner_dict = dict((item["id"], item) for item in londoners)
    nearby_dict = dict((item["id"], item) for item in nearby)
    results = {}
    results.update(londoner_dict)
    results.update(nearby_dict)
    return list(results.values())


def get_haversine(latX, lonX, latY, lonY):

    diffLat = radians(latY - latX)
    diffLon = radians(lonY - lonX)
    latX = radians(latX)
    latY = radians(latY)

    a = sin(diffLat / 2)**2 + cos(latX) * cos(latY) * sin(diffLon / 2)**2
    c = 2 * asin(sqrt(a))

    return R * c
