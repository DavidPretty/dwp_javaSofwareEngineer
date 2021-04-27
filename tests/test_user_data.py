import mysite.flaskr.user_data as user_data
import pytest
from mock import patch
import json
import os

def get_mock_json(url):
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
    return data

def get_mock_londoners():
    return get_mock_json("https://bpdts-test-app.herokuapp.com/city/London/users")


@patch("mysite.flaskr.user_data.requests.get")
def test_get_londoners_returns_status_ok(mock_get_londoners):
    mock_get_londoners.return_value.ok = True
    londoners = user_data.get_londoners()
    assert(londoners.ok)

@patch("mysite.flaskr.user_data.requests.get")
def test_get_londoners_returns_json(get_mock_json):
    londoners = user_data.get_londoners()
    try:
        londoners.json
    except ValueError:
        pytest.fail("output does not contain valid JSON")

@patch("mysite.flaskr.user_data.requests.get")
def test_get_users_not_return_none(get_mock_json):
    users = user_data.get_users()
    assert not users is None

@patch("mysite.flaskr.user_data.requests.get")
def test_get_londoners_not_return_none(get_mock_json):
    londoners = user_data.get_londoners()
    assert not londoners is None
