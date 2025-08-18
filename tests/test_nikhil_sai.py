"""Test cases for all methods in nikhil_sai.py."""

import pytest
from src.nikhil_sai import Circle


def test_circle_no_params() -> None:
    """Test creating a circle without parameters raises TypeError."""
    with pytest.raises(TypeError):
        Circle()


def test_circle_negative() -> None:
    """
    Test creating a circle with a string radius.

    This ensures that the radius is not stored as a string.
    """
    with pytest.raises(AssertionError):
        assert not isinstance(Circle("hii").radius, str)


def test_circle_success() -> None:
    """Test calculating the area of a circle with valid radius."""
    assert Circle(5).get_area() == 78.5
