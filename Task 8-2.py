class Circle:
    def __init__(self, radius):
        # Private variable
        self.__pi = 3.141
        self.radius = radius

    def calculate_area(self):
        # Using the private variable
        area = self.__pi * (self.radius**2)
        return area

    def calculate_circumference(self):
        # Using the private variable
        circumference = 2 * self.__pi * self.radius
        return circumference


# Creating an instance of the Circle class
circle_instance = Circle(radius=5)

# Accessing methods that use the private variable
area = circle_instance.calculate_area()
circumference = circle_instance.calculate_circumference()

# Printing the results
print("Area:", area)
print("Circumference:", circumference)
