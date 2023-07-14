from abstraction.triangle import Triangle

if __name__ == "__main__":
    # Create a Triangle object
    triangle = Triangle(3, 4, 5)

    # Calculate and print the area
    area = triangle.area()
    print("Area:", area)

    # Calculate and print the perimeter
    perimeter = triangle.perimeter()
    print("Perimeter:", perimeter)
