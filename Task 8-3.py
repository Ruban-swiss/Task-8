class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the shape.
        """
        return self.length * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        return 2 * (self.length + self.width)


# Example usage:
# Create an instance of the Shape class with specific dimensions
rectangle = Shape(5, 8)

# Calculate and print the area and perimeter
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
