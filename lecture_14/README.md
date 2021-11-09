# OOP with Python️

## Table of contents 📜

- [Polymorphism](#polymorphism)
- [Magic methods](#magic-methods)

## Polymorphism

Polymorphism is the use of a single type entity (methods, objects, operators) to represent different types of behaviour.

We have already seen that behaviour with the operator `+` (addition)

```python
# The operator + works with numbers
print(7 + 8)  # >>> 15
# But it also works for other types of objects
print("Hello" + " " + "World")  # >>> Hello World
```

Some functions have the same properties as well.

```python
# The function len() can be used to get the length of a list
print(len([1, 2, 3]))  # >>> 3
# But it can also be used to get the length of a string
print(len("Hello World"))  # >>> 11
```

### Class polymorphism

In `OOP` the polymorphism concept is very important. We can have multiple classes having the same method names and later
on treat them all together by generalizing.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name} - {self.age}")

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


animals = [
    Dog("Pesho", 10),
    Cat("Ivan", 12),
    Cat("Dimitar", 16),
    Dog("Caesar", 40),
]

for animal in animals:
    animal.print_info()
    animal.make_sound()
```

## Magic methods

`Magic methods` in Python are the special methods that start and end with the double underscores. They are also called
dunder methods. `Magic methods` are not meant to be invoked directly by you, but the invocation happens internally from
the class on a certain action. For example, when you add two numbers using the + operator, internally, the `__add__()`
method will be called. [ quoted from [here](https://www.tutorialsteacher.com/python/magic-methods-in-python) ]

```python
num = 40
print(num + 5)  # >>> 45
print(num.__add__(5))  # >>> 45
```

Why do we need that?

```python
class MyInteger:
    def __init__(self, my_value):
        self.my_value = my_value


my_integer1 = MyInteger(40)
my_integer2 = MyInteger(5)
print(my_integer1 + my_integer2)  # >>> TypeError: unsupported operand type(s) for +: 'MyInteger' and 'MyInteger'
```

We can implement a custom behaviour of the operator +

```python
class MyInteger:
    def __init__(self, my_value):
        self.my_value = my_value

    def __add__(self, other):
        return self.my_value + other.my_value


my_integer1 = MyInteger(40)
my_integer2 = MyInteger(5)
print(my_integer1 + my_integer2)  # >>> 45
print(my_integer1.__add__(my_integer2))  # >>> 45
```

#### A list of important magic methods

| Operator signature               | Description                                                   |
|----------------------------------|---------------------------------------------------------------|
| `__add__(self, other)`           |  Gets called on add operation using `+` operator              |
| `__sub__(self, other)`           |  Gets called on subtraction operation using `-` operator      |
| `__mul__(self, other)`           |  Gets called on multiplication operation using `*` operator   |
| `__floordiv__(self, other)`      |  Gets called on floor division operation using `//` operator  |
| `__truediv__(self, other)`       |  Gets called on regular division operation using `/` operator |
| `__mod__(self, other)`           |  Gets called on modulo operation using `%` operator           |
| `__pow__(self, other[, modulo])` |  Gets called on power operation using `**` operator           |
| `__lt__(self, other)`            |  Gets called on comparison using `<` operator.                |
| `__le__(self, other)`            |  Gets called on comparison using `<=` operator.               |
| `__eq__(self, other)`            |  Gets called on comparison using `==` operator.               |
| `__ne__(self, other)`            |  Gets called on comparison using `!=` operator.               |
| `__ne__(self, other)`            |  Gets called on comparison using `!=` operator.               |
| `__ge__(self, other)`            |  Gets called on comparison using `>=` operator.               |
| `__gt__(self, other)`            |  Gets called on comparison using `>` operator.                |

| Attribute magic methods signature | Description                                                             |
|-----------------------------------|-------------------------------------------------------------------------|
| `__getattr__(self, name)`         |  Is called when the accessing attribute of a class that does not exist. |
| `__setattr__(self, name, value)`  |  Is called when assigning a value to the attribute of a class.          |
| `__delattr__(self, name)`         |  Is called when deleting an attribute of a class.                       |

| String magic methods signature   | Description                                                                           |
|----------------------------------|---------------------------------------------------------------------------------------|
| `__str__(self)`                  |  To get called by built-int str() method to return a string representation of a type. |
| `__nonzero__(self)`              |  To get called by built-int bool() method to return True or False.                    |

| Augmented Assignment signature           | Description |
|------------------------------------------|-------------|
| `__iadd__(self, other)`                  |  a += b     |
| `__isub__(self, other)`                  |  a -= b     |
| `__imul__(self, other)`                  |  a *= b     | 
| `__ifloordiv__(self, other)`             |  a //= b    |
| `__idiv__(self, other)`                  |  a /= b     |
| `__imod__(self, other)`                  |  a %= b     |
| `__ipow__(self, other)`                  |  a **=b     |

| Unary operators signature | Description  |
|---------------------------|--------------|
| `__pos__(self)`           |  + object    |
| `__neg__(self)`           |  - object    |
| `__abs__(self)`           |  abs(object) | 

## Problem 01

Create a class `MyPositiveInteger` that implements all required magic methods. The core goal of this class is to stay
always positive. When the value of that integer is to go negative then the sign gets inversed.

> Note: you can use the @property decorator

Example:

```python
print(MyPositiveInteger(10) - MyPositiveInteger(17))  # >>> 7
mpi = MyPositiveInteger(-14)
print(mpi)  # >>> 14
```