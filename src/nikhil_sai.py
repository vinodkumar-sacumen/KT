PI = 3.14

def calculate_area(radius:int) -> float:
    """Find the area of a circle by taking its radius and return a float value"""
    return PI * radius ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        """Return the area of the circle """
        return calculate_area(self.radius)

my_circle = Circle(3)
area = my_circle.get_area()
print(f"The area of the circle is: {area}")
