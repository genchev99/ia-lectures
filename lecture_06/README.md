# Introduction to programing with Python️ - Part 5

## Table of contents 📜

- [Functions](#functions)
- [Exercise](#exercise)

## Functions

#### The basics

- A function is a block of code which only runs when it's called
- Functions can take data in the form of arguments
- Functions can return data
- In python a function is defined using the `def` keyword

```python
def function_name(argument_identifier, other_argument_identifier):
    # body
    returned_value = 10
    return returned_value


# call the function
function_name(20, 30)
```

#### How to use arguments

```python
def greet(name):
    print("Welcome: " + name)


greet("pesho")
greet("gosho")
greet("ivan")
```

#### Multiple arguments

- By default, the functions should be called with the correct number of arguments
- Multiple arguments are separated by a `comma` (arg1, arg2)

```python
def greet_by_full_name(first_name, last_name):
    print("Welcome: " + first_name + " " + last_name)


greet_by_full_name("Ivan", "Dimitrov")
```

#### Default arguments

If you call a function without an argument it will use the default value

```python
def repeat(string_to_repeat, times=1):
    for _ in range(times):
        print(string_to_repeat)


repeat("pesho")
repeat("gosho", 3)
```

#### Return value

All functions in python return a value. To let the function return a value use the `return` keyword.

```python
def addition(x, y):
    return x + y


print("5 + 10 = ", addition(5, 10))
```

You can return the value of a variable defined inside the function

```python
def addition(x, y):
    result = x + y

    return result


print("5 + 10 = ", addition(5, 10))
```

By default, if you don't have a `return` statement the function will return `None`

```python
def no_return_example(x, y):
    result = x * y


print("Is result equal to None?: ", no_return_example(10, 20) is None)
```

#### Keyword arguments and type hinting

```python
def repeat(string_to_repeat: str, times: int) -> str:
    return string_to_repeat * times


print(repeat(times=10, string_to_repeat="*"))
```

## Exercise

### Problem 01

Write a python function that returns the maximum number between three arguments. Write a python program that uses the
function with these arguments and prints the result for each.

1. x=10, y=20, z=30
1. x=12, y=-42, z=8
1. x=5, y=72, z=-7
1. x=`result from (1)`, y=`result from (2)`, z=`result from (3)`

```python
def maximum(x: int, y: int, z: int) -> int:
    pass
```

###### Expected output

> 30
>
> 12
>
> 72
>
> 72

___

### Problem 02

Write a python function that returns the sum of list. Write a python program that uses the function with these arguments
and prints the result for each of them.

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [55, 96, 59, 84, 19, 70, 1, 39, 74, 93, 75, 41, 91, 39, 82, 88, 83, 12, 19, 40]
l = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
```

```python
def my_sum(l: list) -> int:
    pass
```

###### Expected output

> 55
>
> 1160
>
> 146

___

## Problem 03

Write a python function that reverses and returns a number (positive int). Write a python program that uses the function
with these arguments and prints the result for each of them.

```python
number = 5
number = 12
number = 63912
```

```python
def reverse_number(number: int) -> int:
    pass
```

###### Expected output

> 5
>
> 21
>
> 21936

___

## Problem 04

Write a python function that finds and returns the factorial of a number (non-negative int). Write a python program that
uses the function with these arguments and prints the result for each of them.

```python
number = 0
number = 1
number = 5
number = 10
```

```python
def factorial(number: int) -> int:
    pass
```

###### Expected output

> 1
>
> 1
>
> 120
>
> 3 628 800

___

## Problem 05

Write a python function that checks if a number (int) can be found in a list of numbers (ints). Write a python program
that uses the function with these arguments and prints the result for each of them.

```python
list_of_numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
number = -26
number = 1
```

```python
def contains(list_of_numbers: list, number: int) -> bool:
    pass
```

###### Expected output

> True
>
> False

___

## Problem 06

Write a python function that returns the amount of numbers from a list in a given range `[a, b]`. Write a python program
that uses the function with these arguments and prints the result for each of them.

```python
list_of_numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
a = 0
b = 100
```

```python
def count_of_numbers_in_range(list_of_numbers: list, a: int, b: int) -> int:
    pass
```

###### Expected output

> 10

___

## Problem 07

Write a python function that returns the unique numbers from a list of numbers. Write a python program that uses the
function with these arguments and prints the result for each of them.

```python
list_of_numbers = [1, 6, 4, 9, 5, 9, 10, 1, 7, 5, 7, 7, 10, 9, 2, 9, 4, 3, 7, 9]
list_of_numbers = [16, 0, -35, -27, -24, 31, 32, -15, 34, 18, 14, 12, -1, -10, -16, 43, 6, 0, -5, -9, -23, 24, -16, 48,
                   40, 45, 5, 0, 37, 8, 39, 49, -4, 34, 2, 2, 40, 28, -50, 21]
```

```python
def is_unique(list_of_numbers: list, number: int) -> bool:
    pass


def unique_all(list_of_numbers: list) -> list:
    pass
```

###### Expected output

> [1, 2, 3, 4, 5, 6, 7, 9, 10]
>
> [0, 2, 5, 6, 8, 12, 14, 16, 18, 21, 24, 28, 31, 32, 34, 37, 39, 40, 43, 45, 48, 49, -50, -35, -27, -24, -23, -16, -15, -10, -9, -5, -4, -1]

___

## Problem 09

Write a python function that takes a number as an argument and returns `True` if it is `prime` and `False` if not. Write
a python program that uses the function with these arguments and prints the result for each of them.

```python
number = 1
number = 2
number = 3
number = 4
number = 25
number = 524287
```

```python
def is_prime(number: int) -> bool:
    pass
```

###### Expected output

> False
>
> True
>
> True
>
> False
>
> False
>
> True

___

## Problem 10

Write a python function that takes a string as an argument and returns `True` if it is `palindrome` and `False` if not.
Write a python program that uses the function with these arguments and prints the result for each of them.

> Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

```python
string = "pesho"
string = "peshohsep"
string = "123321"
string = "shopenpesho"
```

```python
def is_palindrome(string: str) -> bool:
    pass
```

###### Expected output

> False
>
> True
>
> True
>
> False

___

## Problem 10

Write a python function that takes two numbers `(a, b where a <= b)` as an arguments and returns a list of numbers where
the values are the squared values between a and b `[a, b]`. Write a python program that uses the function with these
arguments and prints the result for each of them.

```python
a = 10
b = 20
```

```python
def squares_in_range(a: int, b: int) -> list:
    pass
```

###### Expected output

> [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

___
