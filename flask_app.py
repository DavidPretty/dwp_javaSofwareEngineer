import requests, urllib3

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
proxies = {
  "http": "proxy.server:3128",
  "https": "proxy.server:3128",
} #specific to Pythonanywhere

@app.route('/')
def index():
    return jsonify(message =  "hello world")

def get_londoners():
    return requests.get("https://bpdts-test-app.herokuapp.com/city/London/users",
    proxies)
