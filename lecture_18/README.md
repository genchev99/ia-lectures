# Interesting conceptions in Python

## Table of contents 📜

- [Recursion](#recursion---recursive-functions)
- [Dictionary](#dictionary---collection)
- [Set](#set---collection)

## Recursion - recursive functions

On abstract level a `recursive function` is a function that calls itself (directly or indirectly). This approach is very
powerful in certain situations because you can define and solve a `complex problem` with a previous easy-to-solve state.

![structure](https://cdn.programiz.com/cdn/farfuture/6i17bRQT6hWIqw9JE5rMMyW527g7It_68T7kSzpIplo/mtime:1591262415/sites/tutorial2program/files/python-recursion-function.png)

To see how a recursion works we can start with the following example.

```python
def countdown(current: int):
    if current == 0:
        return

    print(current)
    countdown(current - 1)
```

As you can see the `state` is passed as `arguments` of the function and every function call is happening with different
values.

What is the `call stack` and how it's related to the recursive functions?

> Note: This image is from JS code, but it's good for our purposes

![call stack](https://miro.medium.com/max/1400/1*rJ2sh-q1deQGGGVG5gYyIQ.png)

```python
import traceback


def one():
    two()


def two():
    three()


def three():
    traceback.print_stack()


one()
```

How does the call stack look in a recursive call? Let's have the same example as before but this time print the stack at
the begging if the function as well.

```python
import traceback


def countdown(current: int):
    traceback.print_stack()

    if current == 0:
        return

    print(current)
    countdown(current - 1)
```

In this case we have this base condition.

```python
if current == 0:
    return
```

If you don't have any base conditions (where the function stops) your function will call itself over and over again
until something gives up. Let's try it out!

```python
def countdown(current: int):
    print(current)
    countdown(current - 1)


countdown(10)
```

Let's try with a bit more complex problem. Do you remember when we implemented a `factorial` function with a loop?

```python
def factorial(n: int):
    result = 1

    for n in range(1, n):
        result *= n

    return result
```

We can do the same thing but with recursion instead. You know that a factorial of `6` for example is the same
as `6 * 5!` which is the same as `6 * 5 * 4!` and so on until we get to `0!` which is equal to `1` (this will be our
base case).

```python
def recursive_factorial(current: int):
    if current == 0:
        return 1

    return current * recursive_factorial(current - 1)
```

```python
recursive_factorial(3)  # 1st call with 3
3 * recursive_factorial(2)  # 2nd call with 2
3 * 2 * recursive_factorial(1)  # 3rd call with 1
3 * 2 * 1 * recursive_factorial(0)  # 4rd call with 0
3 * 2 * 1 * 1  # return from 4rd call as current=0
3 * 2 * 1  # return from 3rd call as current=1
3 * 2  # return from 2nd call
6  # return from 1st call
```

You would ask yourself why do we even need such thing when we can just do it the first way - with loops.

![Towers of Hanoi](https://i.redd.it/df5gjbthkpw61.png)

A very good video on this topic https://www.youtube.com/watch?v=8lhxIOAfDss

```python
def hanoi(disks: int, from_r: str, via: str, to: str):
    if disks == 0:
        return

    hanoi(disks - 1, from_r, to, via)
    print(f"Moving disk from {from_r} to {to}")
    hanoi(disks - 1, via, from_r, to)


if __name__ == '__main__':
    hanoi(4, "A", "B", "C")
```

## Dictionary - collection

Dictionaries are used to store data values in `key:value` pairs.

![dictionary compared to list](https://editor.analyticsvidhya.com/uploads/17699Append-a-Dictionary-to-a-list-in-Python-5-i2tutorials.jpeg)

How to define a dictionary in Python

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(my_dict)
```

Dictionary items are ordered, changeable, and does not allow duplicates. The `items` can be accessed using the `keys` (
similar to the indexes in the lists).

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(my_dict["model"])
```

This will throw an error if the `"model"` key does not exist. You can use the `get()` method instead to handle
non-existing keys gracefully

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(my_dict["pesho"])  # Throws an error
print(my_dict.get("pesho"))  # Returns None
```

Dictionaries don't have duplicative keys!

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2021,
}
print(my_dict)  # the first year will be overwritten by the second one
```

Dictionary values are mutable!

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(my_dict["year"])  # 1964
my_dict["year"] += 1
print(my_dict["year"])  # 1965
```

The type of the dictionaries is `dict`.

```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(my_dict))  # <class 'dict'>
```

## Set - collection

A set is a collection which is unordered, unchangeable (you can remove items and add new items), and unindexed.
They `DO NOT` allow duplicated values. You can create a set in two ways.

As a literal

```python
my_set = {"pesho", "gosho", "ivan"}
```

Or with the `set()` constructor

```python
my_set = set()
my_other_set = set(("pesho", "gosho", "ivan"))
```

You can get the length of the set using the function `len()`

```python
my_set = {"pesho", "gosho", "ivan"}
print(len(my_set))  # 3
```

You can add items with the method `add()`

```python
my_set = set()
my_set.add("pesho")
print(my_set)  # {'pesho'}
```

If you try to add an item that `IS ALREADY PART OF THE SET` nothing will happen

```python
my_set = set()
my_set.add("pesho")
my_set.add("pesho")
print(my_set)  # {'pesho'}
```

The type of `set` is `set`

```python
my_set = set()
print(type(my_set))  # <class 'set'>
```

### Problem 01

Write a function that checks for `duplicates` in a `list`.

> Hint: use dictionary or a set for the implementation

##### Usage:

```python
if __name__ == '__main__':
    has_duplicates([1, 2, 3, 4, 5, 6, 7, 8])  # False
    has_duplicates([1, 2, 3, 4, 5, 6, 7, 5, 8])  # True
```

### Problem 02

Write a function that returns the count of occurrences of the char `a` in a string (passed as argument).

##### Usage:

```python
if __name__ == '__main__':
    count_occurrences_of_a("this is a very boring sentence... Don't you think so! aa")  # 3
```

### Problem 03

Write a function that returns the character with most occurrences in a string (passed as argument).

##### Usage:

```python
if __name__ == '__main__':
    char_with_max_occurrences(
        "this is a very boring sentence... Don't you think so! aa")  # A space - has 10 occurrences
```