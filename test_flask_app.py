import pytest, json

import flask_app as fa

app = fa.app

@pytest.fixture
def client():
    app.config["TESTING"] = True

def test_api_get_returns_json():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.is_json

def test_api_get_returns_londoners():
    londoners = fa.get_londoners()
    response = app.test_client().get("/")
    assert(londoners.json() == response.get_json())

def test_get_londoners_not_return_none():
    londoners = fa.get_londoners()
    assert not londoners is None

def test_get_londoners_returns_status_ok():
    londoners = fa.get_londoners()
    assert(londoners.ok)

def test_get_londoners_returns_json():
    londoners = fa.get_londoners()
    try:
        londoners.json
    except ValueError:
        pytest.fail("output does not contain valid JSON")

def test_get_haversine_distance_greater_than_50_miles():
    assert(fa.get_haversine(50, 0, 51, 0) > 50)

def test_get_haversine_distance_less_than_50_miles():
    assert(fa.get_haversine(50, 0, 50.5, 0) < 50)

def test_get_users_not_return_none():
    users = fa.get_users()
    assert not users is None

def test_get_londoners_and_nearby_not_return_none():
    list = fa.get_londoners_and_nearby()
    assert not list is None

def test_get_londoners_and_nearby_contains_all_users_in_get_londoners():
    londoners = fa.get_londoners()
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



