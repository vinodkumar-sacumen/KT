import pytest
import requests
from one import fetch
from pytest_vcr import VCR


def test_fetch():
    url = "https://api.publicapis.org/entries"
    try:
        data = fetch(url)
        assert data is not None
    except Exception as e:
        pytest.fail(f"error occurred : {str(e)}")


"""the process of adding dummy data called MOCKING"""


def test_fetch_mocks(mocker):
    """create mock response"""
    expected_data = {"key": "value"}
    mock_response = mocker.Mock()
    mock_response.json.return_value = expected_data
    mock_response.raise_for_status.return_value = None

    """patch request.get to return mock response"""

    mocker.patch("requests.get", return_value=mock_response)

    """call the function"""
    result = fetch(url="https://api.publicapis.org/entries")

    """Assertion"""

    assert result == expected_data
    requests.get.assert_called_once_with("https://api.publicapis.org/entries")
    mock_response.raise_for_status.assert_called_once()


def test_fetch_with_mock(mocker):
    url = "https://api.publicapis.org/entries"

    """mock request.get function"""

    mocked_get = mocker.patch("requests.get")
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": "success"}

    response = fetch(url)

    assert response == {"result": "success"}
    mocked_get.assert_called_once_with(url)

    """intialize VCR"""


vcr = VCR(cassette_library_dir="tests/mocks/functions")


@pytest.mark.vcr
def test_fetch_with_vcr():
    url = "https://api.publicapis.org/entries"
    response = fetch(url)

    assert response is not None
    assert isinstance(response, dict)
