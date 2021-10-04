"""
`Reverse` the list. Given this list of numbers:
```python
numbers = [1, 2, 3, 4, 5, 6]
```
Write a python program that will print the list in reversed order.

Expected output
> [6, 5, 4, 3, 2, 1]
"""

numbers = [1, 2, 3, 4, 5, 6]

for i in range(int(len(numbers) / 2)):
    temp = numbers[i]
    reverse_index = -1 - i
    numbers[i] = numbers[reverse_index]
    numbers[reverse_index] = temp

# for i in range(int(len(numbers) / 2)):
#     reverse_index = -1 - i
#     numbers[i], numbers[reverse_index] = numbers[reverse_index], numbers[i]

# reversed(numbers)

print(numbers)
