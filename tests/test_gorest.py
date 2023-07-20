import pytest
from typing import Any
import json
from src.gorest import fetch,user_details,user_list
from tests.mocks.function_gorest import mock_user_details_success,mock_user_list_success

def test_fetch():
    """ Test case for fetch method to check the response of method call """    
    response = fetch('https://gorest.co.in/public/v2/users',"https://gorest.co.in/public/v2/users/")
    assert type(response)==list
    assert response[0]['id']==3786877

def test_user_list():
    """ Test case for user_list method to check the response of api call"""    
    response = user_list('https://gorest.co.in/public/v2/users')
    assert type(response)==list
    assert response[0]==3786877

def test_user_details():
    """ Test case for user_details method to check the response of get call """    
    response = user_details('https://gorest.co.in/public/v2/users/',[3786877])
    assert type(response)==list
    assert response[0]['id']== 3786877

def test_fetch_user_details_mock(mocker:Any)->None:
    """ test case for user_details method using mocks.

    Args:
        mocker (Any): _description_
    """    
    mocker.patch("requests.get", mock_user_details_success)
    response = user_details("test_url1",[3786877])
    assert response[0]['id']==3786877

def test_fetch_user_list_mock(mocker:Any)->None:
    """ test case for user_list method using mocks.

    Args:
        mocker (Any): _description_
    """    
    mocker.patch("requests.get", mock_user_list_success)
    response = user_list("test_url1")
    assert response[0]==3786877