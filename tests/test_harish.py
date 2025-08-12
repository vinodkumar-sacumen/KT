"""Unit tests for the Math class with floating-point safe checks."""

import math
import pytest
from src.haris import Math


def test_add() -> None:
    """Test addition of two positive floats."""
    calc = Math(3.0, 2.0)
    assert math.isclose(calc.add(), 5.0)


def test_subtract() -> None:
    """Test subtraction of two positive floats."""
    calc = Math(3.0, 2.0)
    assert math.isclose(calc.subtract(), 1.0)


def test_multiply() -> None:
    """Test multiplication of two positive floats."""
    calc = Math(3.0, 2.0)
    assert math.isclose(calc.multiply(), 6.0)


def test_divide() -> None:
    """Test division of two positive floats."""
    calc = Math(6.0, 3.0)
    assert math.isclose(calc.divide(), 2.0)


def test_divide_by_zero() -> None:
    """Test division by zero raises ZeroDivisionError."""
    calc = Math(6.0, 0.0)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.divide()


def test_divide_zero_numerator() -> None:
    """Test division where numerator is zero."""
    calc = Math(0.0, 3.0)
    assert math.isclose(calc.divide(), 0.0)


def test_divide_negative_numbers() -> None:
    """Test division of two negative floats."""
    calc = Math(-6.0, -3.0)
    assert math.isclose(calc.divide(), 2.0)


def test_add_with_negative_numbers() -> None:
    """Test addition of two negative floats."""
    calc = Math(-3.0, -2.0)
    assert math.isclose(calc.add(), -5.0)


def test_subtract_negative_result() -> None:
    """Test subtraction resulting in a negative value."""
    calc = Math(2.0, 4.0)
    assert math.isclose(calc.subtract(), -3.0)
