import pytest

from flask_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
