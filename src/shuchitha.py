"""
shuchitha.py.

This module contains a simple class that greets a user by name.
"""


class Greeter:
    """A simple class to greet a user."""

    def __init__(self, name: str | int | None) -> None:
        """
        Initialize the Greeter with a name.

        Args:
            name (str | int | None): The name of the user to greet.
        """
        if isinstance(name, list):
            raise ValueError("List is not a valid name")
        if name is None:
            self.name = "Guest"
        else:
            self.name = str(name)

    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, {self.name}! Welcome."

    def get_name(self) -> str:
        """Return the name of the user."""
        return self.name





    #adaded comment
    # added new comment from harish
    #Nikhil sai
    # shuchitha
    #prathyushak adding a comment
