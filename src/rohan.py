"""
    A class to represent a rectangle and perform basic geometric calculation.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
"""
class Rectangle:
    
    def __init__(self, width: float, height: float) -> None:
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

	Returns:
		None: It doesn't return anything.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

obj = Rectangle(10.0, 20.0)
