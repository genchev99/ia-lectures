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
