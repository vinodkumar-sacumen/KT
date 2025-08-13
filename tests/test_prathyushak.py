"""Unit test cases for prathyusha.py file."""


import pytest
from src.prathyushak import ReverseANumber


def test_reverse_success() -> None:
    """Test reversing a positive integer."""
    reverse_number = ReverseANumber(123)
    assert reverse_number.reverse() == 321


def test_reverse_negative_int() -> None:
    """Test reversing a negative integer."""
    reverse_number = ReverseANumber(-124)
    assert reverse_number.reverse() == -421  # Current class returns abs value


def test_reverse_string() -> None:
    """Test giving string name as input."""
    with pytest.raises(TypeError):
        ReverseANumber("Python")


# def test_reverse_no_parameters() -> None:
#     """Test creating without parameters raises TypeError."""
#     with pytest.raises(TypeError):
#         ReverseANumber()   # type: ignore  # noqa: E1120
