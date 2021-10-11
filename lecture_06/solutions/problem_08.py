"""
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

Expected output
> False
> True
> True
> False
> False
> True
"""


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(25))
print(is_prime(524287))
