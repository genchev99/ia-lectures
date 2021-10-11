"""
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

Expected output
> True
> False
"""


def contains(list_of_numbers: list, number: int) -> bool:
    for n in list_of_numbers:
        if n == number:
            return True

    return False


numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
print(contains(numbers, -26))
print(contains(numbers, 1))
