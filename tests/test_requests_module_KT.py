import pytest
from src.requests_module_KT import add_two_numbers, fetch, subtract
from tests.mocks.functions import mock_api_failure, mock_api_success

def test_fetch_success(mocker):
    '''
    Test for successful request response of fetch()
    '''
    mocker.patch("requests.get",mock_api_success)
    response = fetch()
    assert response == 1425

def test_fetch_failure1(mocker):
    '''
    Case 1: Test for response of fetch() when count is not returned
    '''
    mocker.patch("requests.get",mock_api_failure)
    with pytest.raises(AssertionError):
        result = fetch()
        assert result == 1425

def test_fetch_failure2(mocker):
    '''
    Case 2: Test for failure of fetch() by passing an argument
    '''
    with pytest.raises(TypeError):
        result = fetch('aaa')

@pytest.mark.vcr()
def test_fetch():
    '''
    Test fetch() response using vcr
    '''
    result = fetch()
    assert result == 49469
              

def test_add():
    '''
    Test case for add()
    '''
    result = add_two_numbers(100,200)
    assert result == 300

def test_add_failure():
    '''
    Test case for failure of add()
    '''
    with pytest.raises(TypeError):
        result = add_two_numbers(100,'abc')
        
def test_subtract():
    '''
    Test case for add()
    '''
    result = subtract(100,200)
    assert result == 100

def test_add_failure():
    '''
    Test case for failure of add()
    '''
    with pytest.raises(TypeError):
        result = subtract(100,'abc')

def test_no_args():
    '''
    Test case for failure of add_two_numbers() and subtract() when no arguements are passed
    '''
    with pytest.raises(TypeError):
        result_add = add_two_numbers()
        result_sub = subtract()