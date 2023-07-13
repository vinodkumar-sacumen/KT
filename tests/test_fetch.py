"""Test cases python file."""
from typing import Any
import pytest
from src.fetch import fetch, add, divide
from tests.mocks.functions import mock_api_failure, mock_api_success


def test_fetch() -> None:
    """Test case for fetch method."""
    response = fetch(url="https://api.publicapis.org/entries")
    assert response == 1425


def test_fetch_failure() -> None:
    """Test case for fetch method failure."""
    response = fetch(url="https://api.publicapis.org/entriesj")
    assert response == "wrong url"


def test_fetch_mocks(mocker: Any) -> None:
    """Test case for fetch method using mocks."""
    mocker.patch("requests.get", mock_api_success)
    response = fetch(url="test_url")
    assert response == 1425


def test_fetch_mocks_failure(mocker: Any) -> None:
    """Test case for fetch method using mock failure."""
    mocker.patch("requests.get", mock_api_failure)
    response = fetch(url="test_url")
    assert response == "wrong url"


@pytest.mark.vcr
def test_fetch_with_vcr() -> None:
    """Test case for fetch method using pytest_vcr."""
    response = fetch(url="https://api.publicapis.org/entries")
    assert response == 1425


def test_add_success() -> None:
    """Test case for add method."""
    result = add(num1=10, num2=20)
    assert result == 30


def test_add_no_params() -> None:
    """Test case for add method with no params."""
    with pytest.raises(TypeError):
        # pylint: disable = no-value-for-parameter
        add()


def test_add_failure() -> None:
    """Test case for add method for addition failure."""
    with pytest.raises(TypeError):
        add(num1="hello", num2=20)


def test_divide_success() -> None:
    """Test case for division method."""
    result = divide(num1=10, num2=5)
    assert result == 2


def test_divide_no_params() -> None:
    """Test case for divide method with no params."""
    with pytest.raises(TypeError):
        # pylint: disable = no-value-for-parameter
        divide()
