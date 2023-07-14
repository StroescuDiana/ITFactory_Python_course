from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    The abstract base class representing a shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Triangle(Shape):
    """
    A class representing a triangle.
    """

    def __init__(self, xy, yz, xz, height=None):
        """
        Initialize the Triangle object with the given side lengths and optional height.
        """
        self.xy = xy
        self.yz = yz
        self.xz = xz
        self.height = height

    def area(self):
        """
        Calculate the area of the triangle.
        If the height is provided, the area is calculated using base * height / 2 formula.
        If the height is not provided, the area is calculated using Heron's formula.
        """
        if self.height is None:
            s = (self.xy + self.yz + self.xz) / 2  # Calculate the semiperimeter
            area = math.sqrt(s * (s - self.xy) * (s - self.yz) * (s - self.xz))
            return area
        else:
            return self.xy * self.height / 2

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        """
        return self.xy + self.yz + self.xz

# Create a Triangle object
triangle = Triangle(3, 4, 5)

# Calculate and print the area
area = triangle.area()
print("Area:", area)

# Calculate and print the perimeter
perimeter = triangle.perimeter()
print("Perimeter:", perimeter)
