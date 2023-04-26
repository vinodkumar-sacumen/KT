"""Test cases for all methods in demo.py file."""

import pytest
from src.demo import add


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