# OOP with Python️

## Table of contents 📜

- [Classes - revision](#classes---revision)
- [Inheritance](#inheritance)
- [Single inheritance](#single-inheritance)
- [Multiple inheritance](#multiple-inheritance)
- [Multi-level inheritance](#multi-level-inheritance)
- [Method overriding](#method-overriding)
- [Exercise](#exercise)

## Classes - revision

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_identification_string(self) -> str:
        return str(self.age) + "_" + self.name

    def who_am_i(self) -> None:
        print(self.get_identification_string())


person = Person("Pesho", 17)
person.who_am_i()

person2 = Person("Ivan", 34)
person2.who_am_i()
```

## Inheritance

`Inheritance` allows us to define a class (`child`) that inherits all the methods and properties from another
class (`parent`).

`Parent class` is the class being inherited from, also called base class.

`Child class` is the class that inherits from another class, also called derived class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_identification_string(self) -> str:
        return str(self.age) + "_" + self.name

    def who_am_i(self) -> None:
        print(self.get_identification_string())


class Student(Person):
    pass


person = Person("Pesho", 17)
person.who_am_i()

student = Student("Ivan", 20)
student.who_am_i()
```

Constructors in `child` classes

When you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.

```python
class Student(Person):
    def __init__(self, name, age):
# add properties etc.
```

By default when you don't create a constructor the parent constructor will get called. If you decide to create one the
parent constructor will no longer get called. If you still want to call the parent constructor you'll have to do that
explicitly.

```python
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
```

By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit
the methods and properties from its parent.

```python
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
```

You can add additional properties and methods to the `child class`.

```python
class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def get_id(self):
        return self.id
```

## Forms of inheritance

### Single inheritance

This is the simplest form of inheritance where the base (parent) class is extended only by one other class (child)

```python
class Parent:
    def p1(self):
        print("p1")


class Child(Parent):
    def c1(self):
        print("c1")


c = Child()
c.p1()
c.c1()
```

### Multiple inheritance

The inheritance is of type `multiple` when the child class is extending more than one `parent` class. The `child class`
has access to all parents' properties and methods.

In multiple inheritance, if any of the parent classes have a method called in the same way then the child class first
searches the method in its own class. If not found, then it searches in the parent classes depth_first
and `left-right order`.

```python
class Parent1:
    def p1(self):
        print("p1")


class Parent2:
    def p1(self):
        print("p2")


class Parent3:
    def p1(self):
        print("p2")


class Child(Parent1, Parent2, Parent3):
    def c1(self):
        print("c1")


c = Child()
c.p1()
c.p2()
c.p3()
c.c1()
```

### Multi-level inheritance

```python
class Parent:
    def p1(self):
        print("p1")


class Child1(Parent):
    def c1(self):
        print("c1")


class Child2(Child1):
    def c2(self):
        print("c2")


c = Child2()
c.p1()
c.c1()
c.c2()
```

## Method Overriding

The concept of `overriding` is very important in inheritance. It gives the special ability to the child/subclasses to
provide specific implementation to a method that is already present in their parent classes.

```python
class Parent:
    def f1(self):
        print("From parent class")


class Child(Parent):
    def f1(self):
        print("From child class")


obj = Child()
obj.f1()
```

## Exercise

### Problem 01

!Note: the classes design is not a strict as possible. It's for educational purposes.

- Implement a class `Vehicle` with properties `listing_id`, (unique identification number), `price`, `max_speed` (
  maximum possible speed), `number_of_seats` and `year_of_creation`. Also, add these 2 methods `print_vehicle_type()` -
  that prints `Base Vehicle` and `listing_information() -> str` that returns the listing information of the vehicle as a
  string (will be used later on for the listing of the different vehicles)
- Implement a class `Bicycle` that extends `Vehicle` and adds `make` (which is the brand of the bicycle)
  and `is_mountain` (which is true if the bike is a mountain bike) to the properties and override
  the `print_vehicle_type()` method to make it print `Bicycle`. Also, override the other method to return a proper
  listing string (do that for all vehicle types).
- Implement a class `Engine` with properties `fuel_type` (diesel or petrol) and `engine_size` (the size of the engine in
  cubic centimeters)
- Implement a class `MotorVehicle` that extends `Vehicle` and `Engine` and adds properties `is_accident_free`
  and `weight`. Override the `print_vehicle_type()` method to print `Motor Vehicle`
- Implement a class `Car` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the car), `airbags` and `mileage`. Override the `print_vehicle_type()` method to print `Car`
- Implement a class `Motorcycle` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the motorcycle), `is_sport_bike` and `mileage`. Override the `print_vehicle_type()` method to
  print `Motorcycle`
- Implement a class `Boat` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the boat) and `mileage`. Override the `print_vehicle_type()` method to print `Boat`

Implement a class `AutomobileShop` that has a list of available vehicles to purchase. The class has the following
methods too:

- `list_vehicles()` - that prints all available vehicles
- `add_vehicle(vehicle: Vehicle)` - adds a new vehicle to the list
- `remove_vehicle(id)` - removes vehicle by id
- `sort_by_price()` - sorts the list by price

1. Create a new instance of `AutomobileShop`
1. Add a couple of new vehicles to the shop (more than one of each type) using the `add_vehicle` method
1. List the available vehicles
1. Remove a vehicle (which simulates a sale) and list the vehicles again
1. Sort the list of available vehicles by and list them again