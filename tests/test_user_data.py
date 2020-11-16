import mysite.flaskr.user_data as user_data
import pytest
from unittest.mock import patch
from requests import Response
import json
import os



def mock_requests_get(url):
    #code to return new response object
    mock_response = Response()
    mock_response.status_code = 200
    data = object()
    my_path = os.path.abspath(os.path.dirname(__file__))
    if(url == "https://bpdts-test-app.herokuapp.com/city/London/users"):
        path = os.path.join(my_path, "../test_data/all_users.json")
        with open(path) as all_users:
            data = json.load(all_users)
    if(url == "https://bpdts-test-app.herokuapp.com/users"):
        path = os.path.join(my_path, "../test_data/londoners.json")
        with open (path) as londoners:
            data = json.load(londoners)
    mock_response.content = data
    return mock_response


@patch("mysite.flaskr.user_data.requests.get")
def test_get_londoners_returns_status_ok(mock_get_londoners):
    mock_get_londoners.return_value.ok = True
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
