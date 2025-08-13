"""Test cases for all methods in rohan.py file."""

import pytest
from src.rohan import Rectangle


def test_area_success() -> None:
    """Test cases for area method."""
    assert Rectangle(width=10.0, height=20.0).area() == 200.0


def test_area_negative() -> None:
    """Test case for area method using string params."""
    with pytest.raises(TypeError):
        Rectangle(width="hello", height=20.0).area()


def test_perimeter_success() -> None:
    """Test cases for perimeter method."""
    assert Rectangle(width=10.0, height=20.0).perimeter() == 60.0


def test_perimeter_negative() -> None:
    """Test case for perimeter method using string params."""
    with pytest.raises(TypeError):
        Rectangle(width=20.0, height="hi").perimeter()


def test_no_params() -> None:
    """Test case for no params."""
    with pytest.raises(TypeError):
        Rectangle()     # pylint: disable=E1120
