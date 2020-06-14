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

