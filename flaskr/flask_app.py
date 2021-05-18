from flask import Flask, jsonify
from mysite.flaskr.geo import is_within_50_miles_of_London
import mysite.flaskr.user_data as user_data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(get_londoners_and_nearby())

def get_nearby():
    users = user_data.get_users().json()
    nearby = []
    for user in users:
        if is_within_50_miles_of_London(float(user["latitude"]), float(user["longitude"])):
            nearby.append(user)
    return nearby

def get_londoners_and_nearby():
    londoners = user_data.get_londoners().json()
    nearby = get_nearby()
    londoner_dict = dict((item["id"], item) for item in londoners)
    nearby_dict = dict((item["id"], item) for item in nearby)
    results = {}
    results.update(londoner_dict)
    results.update(nearby_dict)
    return list(results.values())
