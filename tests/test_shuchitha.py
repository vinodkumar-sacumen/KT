"""Test cases for the Greeter class in src/shuchitha.py."""

import pytest
from src.shuchitha import Greeter


def test_greet_success() -> None:
    """Test that greeting works for a valid string name."""
    greeter = Greeter("Shuchtha")
    assert greeter.greet() == "Hello, Shuchtha! Welcome."


def test_greet_with_integer() -> None:
    """Test that greeting works when passing an integer."""
    assert Greeter(123).greet() == "Hello, 123! Welcome."


def test_greet_with_empty_string() -> None:
    """Test that greeting works with an empty string."""
    assert Greeter("").greet() == "Hello, ! Welcome."


def test_greet_with_none() -> None:
    """Negative scenario: Passing None should greet as Guest."""
    greeter = Greeter(None)
    assert greeter.greet() == "Hello, Guest! Welcome."


def test_greet_with_list_should_fail() -> None:
    """Negative scenario: Expecting ValueError when passing a list."""
    with pytest.raises(ValueError):
        Greeter(["John", "Doe"])
