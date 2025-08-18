"""Module for calculating the area of a circle."""

PI = 3.14


def calculate_area(radius: int) -> float:
    """
    Find the area of a circle.

    Args:
        radius (int): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return PI * radius ** 2


class Circle:  # pylint: disable=too-few-public-methods
    """A class representing a circle."""

    def __init__(self, radius: int):
        """
        Initialize a Circle instance.

        Args:
            radius (int): The radius of the circle.
        """
        self.radius = radius

    def get_area(self) -> float:
        """
        Return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return calculate_area(self.radius)


my_circle = Circle(5)
area = my_circle.get_area()
print(f"The area of the circle is: {area}")
