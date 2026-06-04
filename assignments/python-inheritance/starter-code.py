"""
Inheritance and Polymorphism - Starter Code

In this assignment, you'll create a shape hierarchy using inheritance and polymorphism.
Complete the classes and test code below.
"""

import math


# Task 1: Create the base Shape class
class Shape:
    """Base class for all shapes."""
    
    def __init__(self, color):
        """Initialize a shape with a color."""
        # TODO: Store the color attribute
        pass
    
    def area(self):
        """Calculate the area of the shape."""
        # TODO: Raise NotImplementedError
        pass
    
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        # TODO: Raise NotImplementedError
        pass
    
    def describe(self):
        """Return a description of the shape."""
        # TODO: Return a string description
        pass


# Task 2: Implement the Circle class
class Circle(Shape):
    """A circle shape."""
    
    def __init__(self, color, radius):
        """Initialize a circle with a color and radius."""
        # TODO: Call the parent class __init__
        # TODO: Store the radius attribute
        pass
    
    def area(self):
        """Calculate the area of the circle."""
        # TODO: Return π * r²
        pass
    
    def perimeter(self):
        """Calculate the circumference of the circle."""
        # TODO: Return 2 * π * r
        pass
    
    def describe(self):
        """Return a description of the circle."""
        # TODO: Return a string like "Circle with radius 5"
        pass


# Task 3: Implement the Rectangle class
class Rectangle(Shape):
    """A rectangle shape."""
    
    def __init__(self, color, width, height):
        """Initialize a rectangle with a color, width, and height."""
        # TODO: Call the parent class __init__
        # TODO: Store the width and height attributes
        pass
    
    def area(self):
        """Calculate the area of the rectangle."""
        # TODO: Return width * height
        pass
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        # TODO: Return 2 * (width + height)
        pass
    
    def describe(self):
        """Return a description of the rectangle."""
        # TODO: Return a string like "Rectangle with width 4 and height 6"
        pass


# Task 4: Test polymorphism
if __name__ == "__main__":
    # Create shape instances
    # TODO: Create a Circle instance with color "red" and radius 5
    # TODO: Create a Rectangle instance with color "blue", width 4, height 6
    
    # Store shapes in a list
    # TODO: Create a list called 'shapes' and add your circle and rectangle
    
    # Demonstrate polymorphism
    # TODO: Loop through the shapes list
    # TODO: For each shape, call describe(), area(), and perimeter()
    # TODO: Print the results in a readable format
    
    # Example output:
    # Circle with radius 5
    # Area: 78.54
    # Perimeter: 31.42
    #
    # Rectangle with width 4 and height 6
    # Area: 24
    # Perimeter: 20
    pass
