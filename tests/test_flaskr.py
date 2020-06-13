import pytest
@pytest.fixture
def client():
    flaskr.app.config["TESTING"] = True

