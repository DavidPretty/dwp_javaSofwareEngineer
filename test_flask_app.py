import pytest

import flask_app as fa

app = fa.app

@pytest.fixture
def client():
    app.config["TESTING"] = True

def test_get_json(): #Test the get method returns json
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.is_json

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