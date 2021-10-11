"""
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
Expected output
> 1
> 1
> 120
> 3 628 800
"""


def factorial(number: int) -> int:
    result = 1
    while number > 1:
        result *= number
        number -= 1

    return result


print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(10))
