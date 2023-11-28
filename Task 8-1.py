import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self, radius):
        return math.pi * radius**2

    def calculate_circumference(self, radius):
        return 2 * math.pi * radius

    def process_circle_data(self):
        for radius in self.radius_list:
            area = self.calculate_area(radius)
            circumference = self.calculate_circumference(radius)

            print(f"For a circle with radius {radius}:")
            print(f"   Area: {area:.2f}")
            print(f"   Circumference: {circumference:.2f}")
            print()

# Example usage with the given list
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)
circle_instance.process_circle_data()
