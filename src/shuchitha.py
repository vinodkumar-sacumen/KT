"""
greeting.py

This module contains a simple class that greets a user by name.
"""


class Greeter:
    """
    A simple class to greet a user.
    """

    def __init__(self, name):
        """
        Initialize the Greeter with a name.

        Args:
            name (str): The name of the user to greet.
        """
        self.name = name

    def greet(self):
        """
        Print a greeting message.
        """
        print(f"Hello, {self.name}! Welcome.")


# Object creation and method call
greeter = Greeter("Shuchitha")
greeter.greet()
