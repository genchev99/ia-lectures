"""
Write a Python program to remove a specified item using the index from an array. Given this list of numbers:
```python
numbers = [1, 2, 3, 4, 5, 6]
index_to_remove = 3
```

Expected output
> [1, 2, 3, 5, 6]
"""

numbers = [1, 2, 3, 4, 5, 6]
index_to_remove = 3

numbers.pop(index_to_remove)

print(numbers)
