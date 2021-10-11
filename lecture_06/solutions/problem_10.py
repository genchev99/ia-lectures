"""
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

Expected output
> [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
"""


def squares_in_range(a: int, b: int) -> list:
    squares = []
    for i in range(a, b + 1):
        squares.append(i ** 2)

    return squares


print(squares_in_range(10, 20))
