class MyClass:
    # Class variable
    class_variable = "I am a class variable"

    def __init__(self, initial_value):
        # Instance variable
        self.instance_variable = initial_value

    def get_instance_variable(self):
        return self.instance_variable

    def set_instance_variable(self, new_value):
        self.instance_variable = new_value

    def print_class_variable(self):
        print(MyClass.class_variable)


# Creating an instance of MyClass
my_instance = MyClass("Initial Value")

# Accessing instance variable
print("Instance Variable:", my_instance.get_instance_variable())

# Modifying instance variable
my_instance.set_instance_variable("New Value")
print("Modified Instance Variable:", my_instance.get_instance_variable())

# Accessing class variable
my_instance.print_class_variable()
