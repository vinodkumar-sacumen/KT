import pytest
from src.fetch import fetch
from tests.mocks.functions import mock_api_success, mock_api_failure


def test_fetch():
    
    response = fetch(url="https://api.publicapis.org/entries")
    with pytest.raises(AttributeError):
        assert response.status_code == 200


def test_fetch_mocks(mocker):
    mocker.patch("requests.get", mock_api_success)
    response = fetch(url="test_url")
    with pytest.raises(AttributeError):
        assert response.status_code == 200
    
   
def test_fetch_mocks_failure(mocker):
    mocker.patch("requests.get", mock_api_failure)
    response = fetch(url="test_url")
    with pytest.raises(AttributeError):
        assert response.status_code == 403

    
@pytest.mark.vcr
def test_fetch_with_vcr():
    response = fetch(url="https://api.publicapis.org/entries")
    with pytest.raises(AttributeError):
        assert response.status_code == 200


    
