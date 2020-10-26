import mysite.flaskr.user_data as user_data
import pytest
from unittest import mock

def mock_requests_get(url):
    #code to return new request object
    pass


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
