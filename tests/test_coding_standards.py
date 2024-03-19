"""Test cases for coding standards module."""
import pytest
from src.coding_standards import add_two_numbers, fetch, subtract
from tests.mocks.functions import mock_api_failure, mock_api_success
from typing import Any


def test_fetch_success(mocker: Any) -> None:
    """Test case for success of fetch() when count is retruned.

    Args:
        mocker (any): Mocker to patch the api call.
    """
    mocker.patch("requests.get", mock_api_success)
    response = fetch()
    assert response == 1425


def test_fetch_failure1(mocker: Any) -> None:
    """Test case for failure of fetch() when count is not returned.

    Args:
        mocker (any): Mocker to patch api call.
    """
    mocker.patch("requests.get", mock_api_failure)
    with pytest.raises(AssertionError):
        result = fetch()
        assert result == 1425


@pytest.mark.vcr()
def test_fetch() -> None:
    """Test case for success of fetch() using vcr."""
    result = fetch()
    assert result == 49469


def test_add() -> None:
    """Test case for success of add()."""
    result = add_two_numbers(100, 200)
    assert result == 300


def test_add_failure() -> None:
    """Test case for failure of add()."""
    with pytest.raises(TypeError):
        add_two_numbers(100, 'abc')


def test_subtract() -> None:
    """Test case for success of subtract()."""
    result = subtract(100, 200)
    assert result == 100


def test_subtract_failure() -> None:
    """Test case for failure of subtract()."""
    with pytest.raises(TypeError):
        subtract(100, 'abc')
