import pytest
from src.fetch import add, divide, fetch

from tests.mocks.functions import mock_api_success, mock_api_failure


def test_fetch():
    response = fetch(url="https://api.publicapis.org/entries")
    assert response == 1425


def test_fetch_failure():
    response = fetch(url="https://api.publicapis.org/entriesj")
    assert response == "wrong url"


def test_fetch_mocks(mocker):
    mocker.patch("requests.get", mock_api_success)
    response = fetch(url="test_url")
    assert response == 1425


def test_fetch_mocks_failure(mocker):
    mocker.patch("requests.get", mock_api_failure)
    response = fetch(url="test_url")
    assert response == "wrong url"


@pytest.mark.vcr
def test_fetch_with_vcr():
    response = fetch(url="https://api.publicapis.org/entries")
    assert response == 1425


def test_add_success():
    result = add(num1=10, num2=20)
    assert result == 30


def test_add_no_params():
    with pytest.raises(TypeError):
        add()


def test_add_failure():
    result = add(num1=5, num2="Hi")
    assert result is None


def test_divide_success():
    result = divide(num1=10, num2=5)
    assert result == 2.0


def test_divide_no_params():
    with pytest.raises(TypeError):
        divide()


def test_divide_failure():
    result = divide(num1=5, num2=0)
    assert result is None
