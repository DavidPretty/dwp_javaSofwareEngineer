import requests, urllib3

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(message =  "hello world")

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")
