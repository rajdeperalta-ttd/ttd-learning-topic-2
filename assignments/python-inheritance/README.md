# 📘 Assignment: Inheritance and Polymorphism

## 🎯 Objective

Learn how to create class hierarchies using inheritance and implement polymorphism by overriding methods in subclasses. You'll build a shape system where different shapes inherit from a base class and implement their own behavior for calculating area and perimeter.

## 📝 Tasks

### 🛠️ Create a Shape Hierarchy

#### Description
Design a base `Shape` class that other shapes will inherit from. This class should define the interface that all shapes must implement, including methods for calculating area and perimeter, as well as a method to describe the shape.

#### Requirements
The `Shape` base class should:

- Have an abstract method `area()` that raises `NotImplementedError`
- Have an abstract method `perimeter()` that raises `NotImplementedError`
- Have a method `describe()` that returns a string description of the shape
- Store a color attribute in the `__init__` method


### 🛠️ Implement the Circle Class

#### Description
Create a `Circle` class that inherits from `Shape`. Override the `area()` and `perimeter()` methods to calculate the circle's area and circumference based on its radius.

#### Requirements
The `Circle` class should:

- Inherit from `Shape`
- Store a `radius` attribute
- Override `area()` to return $\pi r^2$
- Override `perimeter()` to return $2\pi r$ (circumference)
- Override `describe()` to return a string like "Circle with radius 5"


### 🛠️ Implement the Rectangle Class

#### Description
Create a `Rectangle` class that inherits from `Shape`. Override the `area()` and `perimeter()` methods to calculate the rectangle's area and perimeter based on its width and height.

#### Requirements
The `Rectangle` class should:

- Inherit from `Shape`
- Store `width` and `height` attributes
- Override `area()` to return width × height
- Override `perimeter()` to return 2 × (width + height)
- Override `describe()` to return a string like "Rectangle with width 4 and height 6"


### 🛠️ Test Polymorphism

#### Description
Write code that creates instances of `Circle` and `Rectangle`, stores them in a list, and demonstrates polymorphism by calling the same methods on different shape types.

#### Requirements
Your test code should:

- Create at least one `Circle` and one `Rectangle` instance
- Store them in a list
- Loop through the list and call `area()`, `perimeter()`, and `describe()` on each shape
- Print the results in a readable format
