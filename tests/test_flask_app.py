import pytest
from mock import patch, Mock, PropertyMock

import mysite.flaskr.flask_app as fa
import mysite.flaskr.user_data as user_data
from mysite.tests.test_user_data import get_mock_londoners


app = fa.app

mockLondonersJSON = Mock()
mockLondonersJSON.return_value = get_mock_londoners()

@pytest.fixture
def client():
    app.config["TESTING"] = True


@patch("mysite.flaskr.user_data.requests.get")
def test_api_get_returns_status_OK(mock_response):
    type(mock_response).status_code = PropertyMock(return_value = 200)
    assert mock_response.status_code == 200

@patch("mysite.flaskr.user_data.get_londoners.json", mockLondonersJSON)
def test_api_get_returns_json():
    response = app.test_client().get('/')
    assert response.is_json

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
