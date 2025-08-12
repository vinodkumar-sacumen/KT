"""A class to represent a rectangle and perform basic geometric calculation."""


class Rectangle:
    """Represents a rectangle.

    This class stores the width and height of a rectangle and provides
    a method to calculate its area.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


obj = Rectangle(15.62, 50.0)