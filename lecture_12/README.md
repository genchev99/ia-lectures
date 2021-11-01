# OOP with Python️

## Table of contents 📜

- [Class properties (attributes)](#class-properties-attributes)
    - [Basic usage](#basic-usage)
    - [Class attribute vs Instance attribute](#class-attribute-vs-instance-attribute)
    - [Private vs Public attributes](#private-vs-public-attributes)
    - [The `@property` decorator](#the-property-decorator)

## Class properties (attributes)

### Basic usage

Class (Instance) properties are `variables` defined inside the class definition. They have names and types and can only
be accessed via the `class` or an `instance of the class`.

```python
# Creates a new Class 'Example' with one instance attribute
class Example:
    def __init__(self, example_variable):
        self.example_variable = example_variable


example = Example(21)
# You can directly access the value of the variable with . (dot)
print(example.example_variable)  # >>> 21
# You can directly change the value of the variable
example.example_variable += 21
print(example.example_variable)  # >>> 42

# You can also attach new properties to the instance
# but it's highly unlikely in a real world situation
example.new_variable = 10
example.other_variable = 11
print(example.new_variable)
```

### Class attribute vs Instance attribute

An `instance attribute` is a Python variable belonging to one, and only one, object. This variable is only accessible in
the scope of this object, and it is defined inside the constructor.

```python
class Example:
    def __init__(self):
        self.instance_attribute = 10
```

A `class attribute` is a Python variable that belongs to a class rather than a particular object. It is shared between
all the objects of this class, and it is defined outside the constructor

```python
class Example:
    class_attribute = 10

    def __init__(self):
        pass
```

The `instance_attribute` is only accessible from the scope of an `object` (instance). The `class_attribute is accessible
as both a property of the class and the object.

```python
class Example:
    class_attribute = 10

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute


example01 = Example(21)
example02 = Example(42)

# Prints the instance attributes of each instance (you can see that they are different)
print(example01.instance_attribute)  # >>> 21
print(example02.instance_attribute)  # >>> 42

# Prints the class attributes. You can see that they are the same.
print(example01.class_attribute)  # >>> 10
print(example02.class_attribute)  # >>> 10

# You can also access the class attributes from the class itself.
print(Example.class_attribute)  # >>> 10
```

`Class attributes` can be changed, but they have different behavior when changed from a `class` and from an `instance`.

```python
class Example:
    class_attribute = 10

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute


example01 = Example(21)
example02 = Example(42)

# When the class attribute value is changed from the Class it will be changed for the instance as well.
Example.class_attribute = 50

print(Example.class_attribute)  # >>> 50
print(example01.class_attribute)  # >>> 50
print(example02.class_attribute)  # >>> 50

# This line will "transform" the variable class_attribute to be an 'instance attribute'.
# Remember how we 'attached' a new variable to the instance before.
# The same thing is happening now too.
example01.class_attribute = -50
print(Example.class_attribute)  # >>> 50
print(example01.class_attribute)  # >>> -50 
print(example02.class_attribute)  # >>> 50
```

### Private vs Public attributes

In OOP, we `encapsulate` by binding the `data` and `functions` which operate on that data into a `single unit`, the
class. By doing so, we can `hide private details` of a class from the `outside world` and only expose functionality that
is important for interfacing with it. When a class does not allow calling code access to its private data directly, we
say that it is well encapsulated.

```python
class Example:
    def __init__(self):
        self.__private_instance_attribute = 10
        self._protected_instance_attribute = 20
        self.public_instance_attribute = 30

    def __private_method(self):
        print("hello from a private method")

    def _protected_method(self):
        print("hello from a protected method")

    def public_method(self):
        print("hello from a public method")

    def acessing_members(self):
        print(self.public_instance_attribute)
        self.public_method()
        print(self._protected_instance_attribute)
        self._protected_method()

        # you can see that private members can be accesses within the class
        print(self.__private_instance_attribute)
        self.__private_method()


example = Example()
print(example.public_instance_attribute)  # >>> 30
example.public_method()  # >>> hello from a public method
print(example._protected_instance_attribute)  # >>> 20 
example._protected_method()  # >>> hello from a protected method

# You can see that you can't directly access private members from outside of the class

print(example.__private_instance_attribute)
# >>> AttributeError: 'Example' object has no attribute '__private_instance_attribute' 
example._private_method()  # >>> hello from a protected method
# AttributeError: 'Example' object has no attribute '_private_method'
```

### The `@property` decorator

Direct accessing

```python
class Temperature:
    def __init__(self, temperature: float):
        # Stores the temperature in Celsius
        self.temperature = temperature

    def in_fahrenheit(self) -> float:
        print("Transforming the temperature from Celsius to Fahrenheit")
        return (self.temperature * 1.8) + 32


temperature_instance = Temperature(36.5)
print(temperature_instance.in_fahrenheit())
temperature_instance.temperature = 39.5
print(temperature_instance.in_fahrenheit())
```

Using getters and setters to validate the values.

```python
def celsius_to_fahrenheit(temperature: float) -> float:
    return (temperature * 1.8) + 32


class Temperature:
    def __init__(self, temperature: float):
        # Stores the temperature in Celsius
        self._temperature = temperature

    def in_fahrenheit(self) -> float:
        print("Transforming the temperature from Celsius to Fahrenheit")
        return celsius_to_fahrenheit(self._temperature)

    def set_temperature(self, new_temperature: float):
        # If the new temperature is below the absolute zero in fahrenheit we consider it to be invalid!
        if celsius_to_fahrenheit(new_temperature) < -273.15:
            raise ValueError("The temperature can't be below the absolut zero")

        # otherwise we set the new value
        self._temperature = new_temperature

    def get_temperature(self):
        return self._temperature


temperature_instance = Temperature(36.5)
print(temperature_instance.in_fahrenheit())
temperature_instance.set_temperature(39.5)
print(temperature_instance.in_fahrenheit())
temperature_instance._temperature = -300
print(temperature_instance.in_fahrenheit())
```

Using the @property decorator

```python
def celsius_to_fahrenheit(temperature: float) -> float:
    return (temperature * 1.8) + 32


class Temperature:
    def __init__(self, temperature: float):
        # Stores the temperature in Celsius
        self.temperature = temperature

    def in_fahrenheit(self) -> float:
        print("Transforming the temperature from Celsius to Fahrenheit")
        return celsius_to_fahrenheit(self.temperature)

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temperature: float):
        # If the new temperature is below the absolute zero in fahrenheit we consider it to be invalid!
        if celsius_to_fahrenheit(new_temperature) < -273.15:
            raise ValueError("The temperature can't be below the absolut zero")

        # otherwise we set the new value
        self.__temperature = new_temperature


temperature_instance = Temperature(36.5)
print(temperature_instance.in_fahrenheit())
temperature_instance.temperature = 39.5
print(temperature_instance.in_fahrenheit())
```

## Exercise

### Problem 01

Create a class Person that has two instance attributes `first_name` and `last_name`. Create a new instance of that
class. Directly accessing the attributes change the value of `first_name` to `David`
and `last_name` to `Alexander`. After that print the new values on the standard output.

### Problem 02

Create a class Student that has the following attributes:

- `first_name` - the first name of the student
- `last_name` - the last name of the student
- `id` - the class id of the student (a positive integer)
- `grades` - a list of the student grades

Using a class attribute find a way to make the id `auto incremental`
(when a new student instance is create the id will be autogenerated)

Example:

```python
class Student:
    pass


# Create a new list of students
students = [
    Student("Ivan", "Dimitrov"),
    Student("Dimitar", "Ivanov"),
]

for student_index in range(len(students)):
    assert students[student_index].id == student_index + 1
```

### Problem 03

Reuse the class definition from `Problem 02`.

- make `grades` a private property
- make `first_name` and `last_name` protected

- Create a new private method `__average()` that calculates the average grade of the student.
- Create a new public method `add_grade(grade: float)` that adds a new grade to the student grades (make sure that the
  grade is valid).
- Create a new public method `get_score() -> str:` that returns information for the student in the following format
  `"{id}, {first_name} {last_name}, {average_grade}"`

Make a couple of students and store them in a list. Add various grades to them and for each of them print their `score`.

### Problem 04

Create a class Person with `first_name` and `last_name`. Create a new `@property blood_type (str)` for that class and a
setter. Inside that setter make sure that the only allowed blood types are ["A", "B", "AB", "0"]. In case the value is
something else make sure to throw a proper exception!

Create a method `print_person_info()` which prints the person information in the following
format `"{first_name} {last_name} - {blood_type}"`

Create a new `Person` with each type of blood and print each of them.

Create one with blood type `"AO"` - it should throw an error.
