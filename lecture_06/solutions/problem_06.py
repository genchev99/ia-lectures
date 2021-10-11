"""
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

Expected output
> 10
"""


def count_of_numbers_in_range(list_of_numbers: list, a: int, b: int) -> int:
    count = 0
    for number in list_of_numbers:
        if a <= number <= b:
            count += 1

    return count


numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
print(count_of_numbers_in_range(numbers, 0, 100))
