"""
Write a Python program to insert a new item before the `second` element in an existing array. Given this list of
numbers:
```python
numbers = [1, 2, 3, 4, 5, 6]
number_to_insert = 42
```

Expected output
> [1, 42, 2, 3, 4, 5, 6]
"""

numbers = [1, 2, 3, 4, 5, 6]
number_to_insert = 42

numbers.insert(1, number_to_insert)

print(numbers)
