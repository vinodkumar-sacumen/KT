import pytest
import requests
from src.one import fetch
from pytest_vcr import VCR


def test_fetch():
    url = "https://api.publicapis.org/entries"
    with pytest.raises(AssertionError):
        assert fetch(url) is None


"""the process of adding dummy data called MOCKING"""


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
