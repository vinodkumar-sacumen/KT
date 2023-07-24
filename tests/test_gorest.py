import pytest
from typing import Any
import json
from src.gorest import fetch,user_details,user_list
from tests.mocks.function_gorest import mock_user_details_success,mock_user_list_success,mock_user_details_failure,mock_user_list_failure

def test_fetch_user_details_mock(mocker:Any)->None:
    """ test case for user_details method using mocks.

    Args:
        mocker (Any): A mocker
    """    
    mocker.patch("requests.get", mock_user_details_success)
    response = user_details("test_url1",[12345])
    assert response[0]['id']==12345

def test_fetch_user_list_mock(mocker:Any)->None:
    """ test case for user_list method using mocks.

    Args:
        mocker (Any): A mocker
    """    
    mocker.patch("requests.get", mock_user_list_success)
    response = user_list("test_url1")
    assert response[0]==12345

def test_user_details_mocks_failure(mocker: Any) -> None:
    """Test case for fetch user details method using failure mock response.

    Args:
        mocker (Any): A mocker
    """
    mocker.patch("requests.get", mock_user_details_failure)
    response = user_details("test_url",[12345])
    assert response == []

def test_user_list_mocks_failure(mocker: Any) -> None:
    """Test case for fetch user list method using failure mock response.

    Args:
        mocker (Any): A mocker
    """
    mocker.patch("requests.get", mock_user_list_failure)
    response = user_list("test_url")
    assert response == []