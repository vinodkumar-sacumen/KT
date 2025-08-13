"""Test cases for all methods in demo.py file."""

from typing import Any

import pytest

from src.demo import add, fetch
from tests.mocks.functions import mock_api_failure, mock_api_success


def test_add_success()-> None:
    """Test cases for add method."""
    result = add(num1=10, num2=20)
    assert result == 30

def test_add_negative()-> None:
    """test case for add method using string params"""
    with pytest.raises(TypeError):
        add(num1="hello", num2=20)

def test_add_no_params()-> None:
    """Test case for no params."""
    with pytest.raises(TypeError):
        add()

def test_fetch()-> None:
    """Test case for fetch method to check on api response."""
    response = fetch(url="https://api.publicapis.org/entries")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 1425

def test_fetch_mocks(mocker: Any)-> None:
    """test case for fetch method using mocks.

    Args:
        mocker (Any): A mocker
    """
    mocker.patch("requests.get", mock_api_success)
    response = fetch(url="test_url")
    data = response.json()
    assert response.status_code == 200
    assert data['count'] == 1425


def test_fetch_mocks_failure(mocker: Any) -> None:
    """Test case for fetch method using failure mock response.

    Args:
        mocker (Any): A mocker
    """
    mocker.patch("requests.get", mock_api_failure)
    response = fetch(url="test_url")
    data = response.json()
    assert response.status_code == 403
    assert data['Error'] == "Invalid Authentication"


@pytest.mark.vcr()
def test_fetch_vcr()-> None:
    """Test case for fetch method using VCR"""
    response = fetch(url="https://api.publicapis.org/entries")
    data = response.json()
    assert response.status_code == 200
    assert data['count'] == 1425
