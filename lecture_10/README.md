# OOP with Python️

## Table of contents 📜

- [Classes - revision](#classes-revision)

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

`Inheritance` allows us to define a class (`child`) that inherits all the methods and properties from another class (`parent`).

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

By default when you don't create a constructor the parent constructor will get called.
If you decide to create one the parent constructor will no longer get called. 
If you still want to call the parent constructor you'll have to do that explicitly.

```python
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
```

By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

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
