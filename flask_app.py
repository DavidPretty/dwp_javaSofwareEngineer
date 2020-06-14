import requests

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return jsonify(message =  "hello world")

def getLondoners():
    pass
