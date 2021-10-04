"""
Write a Python program to remove the `first occurrence of a specified element` from an array. Given this list of
numbers:

```python
numbers = [1, 2, 3, 4, 5, 3, 6, 3]
number_to_remove = 3
```

Expected output
> [1, 2, 4, 5, 3, 6, 3]
"""

numbers = [1, 2, 3, 4, 5, 3, 6, 3]
number_to_remove = 3
first_index = -1

for x in range(len(numbers)):
    if numbers[x] == number_to_remove:
        first_index = x
        break

if first_index != -1:
    numbers.pop(first_index)

print(numbers)
