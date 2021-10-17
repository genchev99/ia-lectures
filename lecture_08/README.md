# OOP with Python️

## Table of contents 📜

- [Classes](#classes)
- [Exercise](#exercise)

## Classes

Python is an `object-oriented language` and almost everything is an object with properties and methods.

A `Class` is like `blueprint` for creating objects.

A simple `class` looks like that.

```python
class ClassName:
    attribute_name = "attribute value"


class_instance = ClassName()
print(class_instance.attribute_name)
```

### Constructors

All classes have a function called `__init__()`, which is always executed when the class is being initiated.

Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when
the object is being created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Pesho", 17)

print(p1.name)
print(p1.age)
```

### Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self) -> None:
        print("Hello my name is " + self.name)


p1 = Person("Pesho", 17)
p1.my_func()
```

## Exercise

### Problem 01

Write a Python class named Student with two attributes student_id, student_name. Create a constructor for these values.
Create a method `display()` to display the entire attribute and their values in Student class.

```python
class Student:
    def __init__(self):
        pass

    def display(self):
        pass


student = Student(42, "pesho")
student.display()
```

### Problem 02

Write a Python class `MyMath` and implement `pow`, `factorial`, `floor`, `difference`.

```python
class MyMath:
    def pow(self, x: float, n: float):
        pass

    def factorial(self, x: int):
        pass

    def floor(self, x: float):
        pass

    def difference(self, a: float, b: float):
        pass


m = MyMath()
print(m.factorial(5))  # 120
print(m.floor(5.3))  # 5
print(m.pow(2, 10))  # 1024
print(m.difference(10, 6))  # 4
```

### Problem 03

Write a Python class named `Rectangle` constructed by a `length` and `width` and a method which will compute the area of
a rectangle.

```python
class Rectangle:
    def __init__(self, length: float, width: float):
        pass

    def area(self) -> float:
        pass
```

### Problem 04

Write a Python class named `Circle` constructed by a `radius` and two methods which will compute the area and the
perimeter of a circle

```python
class Circle:
    def __init__(self, radius: float):
        pass

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass
```

### Problem 05

Write a Python class named `Point` constructed by an `x` and `y` coordinates. Write a Python class named `Circle`
constructed by a `radius` and a `center Point (x, y)`
and add the following methods

- `area()` - returns the area of the circle
- `perimeter()` - returns the perimeter of the circle
- `distance(p: Point)` - returns the distance from the center to a Point passed as an argument
- `position(p: Point)` - returns one of the `p` is in the circle, `0` if it's on the edge and `-1` if it's outside
