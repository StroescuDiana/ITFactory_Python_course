import math

from abstraction.shape import Shape


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
