"""This module provides a Math class to perform basic arithmetic operations."""


class Math:
    """Performs basic arithmetic operations on two float numbers."""

    def __init__(self, first_number: float, second_number: float) -> None:
        """
        Initialize Math object with two numbers.

        Args:
            first_number (float): The first operand.
            second_number (float): The second operand.
        """
        self.first_number = first_number
        self.second_number = second_number

    def add(self) -> float:
        """Return the sum of the two numbers."""
        return self.first_number + self.second_number

    def subtract(self) -> float:
        """Return the difference between the two numbers."""
        return self.first_number - self.second_number

    def multiply(self) -> float:
        """Return the product of the two numbers."""
        return self.first_number * self.second_number

    def divide(self) -> float:
        """
        Return the result of division of the two numbers.

        Raises:
            ZeroDivisionError: If divisor is zero.

        Returns:
            float: Quotient of the division.
        """
        if self.second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.first_number / self.second_number


if __name__ == "__main__":
    calculator = Math(14.0, 7.0)
    print("Addition:", calculator.add())
    print("Subtraction:", calculator.subtract())
    print("Multiplication:", calculator.multiply())
    print("Division:", calculator.divide())
