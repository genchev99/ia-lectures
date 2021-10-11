"""
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
Expected output
> 5
> 21
> 21936
"""
import math


def reverse_number(number: int) -> int:
    result = 0

    while number != 0:
        result = result * 10 + number % 10
        number = int(number / 10)

    return result


print(reverse_number(5))
print(reverse_number(12))
print(reverse_number(63912))
