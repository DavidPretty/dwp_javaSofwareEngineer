import pytest

import flask_app as fa
import user_data

app = fa.app

@pytest.fixture
def client():
    app.config["TESTING"] = True

def test_api_get_returns_json():
    response = app.test_client().get('/')
    assert response.is_json

def test_api_get_returns_status_OK():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_api_get_returns_get_londoners_and_nearby():
    londoners_and_nearby = fa.get_londoners_and_nearby()
    response = app.test_client().get("/")
    assert(londoners_and_nearby == response.get_json())


def test_get_londoners_and_nearby_not_return_none():
    list = fa.get_londoners_and_nearby()
    assert not list is None

def test_get_londoners_and_nearby_contains_all_users_in_get_londoners():
    londoners = user_data.get_londoners()
    combined = fa.get_londoners_and_nearby()
    if (londoners is not None) and (combined is not None):
        londoners = londoners.json()
        londoners_dict = dict((item["id"], item) for item in londoners)
        combined_dict = dict((item["id"], item) for item in combined)
        assert londoners_dict.keys() <= combined_dict.keys()
    else:
        pytest.fail("one of the lists of users is None")

def test_get_londoners_and_nearby_contains_all_users_in_get_nearby():
    nearby = fa.get_nearby()
    combined = fa.get_londoners_and_nearby()
    if (nearby is not None) and (combined is not None):
        nearby_dict = dict((item["id"], item) for item in nearby)
        combined_dict = dict((item["id"], item) for item in combined)
        assert nearby_dict.keys() <= combined_dict.keys()
    else:
        pytest.fail("one of the lists of users is None")
