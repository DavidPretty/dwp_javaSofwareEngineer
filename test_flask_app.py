import pytest

import flask_app

app = flask_app.app

@pytest.fixture
def client():
    app.config["TESTING"] = True

def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == "hello world"