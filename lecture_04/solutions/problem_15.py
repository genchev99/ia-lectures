"""
Bubble sort. Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 7, 0, 8, 4]
```

Expected output
> [0, 1, 2, 3, 4, 4, 7, 8]
"""

numbers = [1, 2, 3, 4, 7, 0, 8, 4]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)
