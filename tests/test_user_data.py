import mysite.flaskr.user_data as user_data
import pytest
from unittest import mock
from requests import Response
import json


def mock_requests_get(url):
    #code to return new response object
    mock_response = Response()
    mock_response.ok = True
    data = object()
    if(url == "https://bpdts-test-app.herokuapp.com/city/London/users"):
        with open("../test_data/all_users.json") as all_users:
            data = json.load(all_users)
    if(url == "https://bpdts-test-app.herokuapp.com/users"):
        with open ("../test_data/londoners.json") as londoners:
            data = json.load(londoners)
    mock_response.content = data
    return mock_response

def test_get_londoners_returns_status_ok():
    londoners = user_data.get_londoners()
    assert(londoners.ok)

def test_get_londoners_returns_json():
    londoners = user_data.get_londoners()
    try:
        londoners.json
    except ValueError:
        pytest.fail("output does not contain valid JSON")

def test_get_users_not_return_none():
    users = user_data.get_users()
    assert not users is None

def test_get_londoners_not_return_none():
    londoners = user_data.get_londoners()
    assert not londoners is None
