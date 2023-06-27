import pytest, requests

from requests import Response
from one import fetch

from mocks.functions import mock_api_success, mock_api_failure


def test_fetch():
    response = fetch(url="https://api.publicapis.org/entries")
    data = response.json()
    count = data["count"]
    assert response.status_code == 200
    assert data["count"] == 1425


"""the process of adding dummy data called MOCKING"""


def test_fetch_mocks(mocker):
    mocker.patch("requests.get", mock_api_success)
    response = fetch(url="test_url")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 1425


def test_fetch_mocks_failure(mocker):
    mocker.patch("requests.get", mock_api_failure)
    response = fetch(url="test_url")
    data = response.json()
    assert response.status_code == 403
    assert data["Error"] == "Invalid Authentication"


@pytest.mark.vcr()
def test_fetch_vcr(s):
    response = fetch(url="https://api.publicapis.org/entries")
    assert response.status_code == 200
