"""
Find the `second biggest` number. Given this list of numbers:
```python
numbers = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
```
Write a python program that will find the `second biggest` number in that list.

Expected output
> 82
"""

numbers = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
biggest = numbers[0]
second_biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number
    elif second_biggest < number <= biggest:
        second_biggest = number

print(second_biggest)
