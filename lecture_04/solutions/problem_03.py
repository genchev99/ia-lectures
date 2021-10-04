"""
`Min` and `Max` in a list. Given this list of numbers:
```python
numbers = [18, 32, 72, 100, 7, 74, 17, 45, 42, 66, 86, 79, 23, 54, 35]
```
Write a python program that will find the `max` and `min` numbers in that list.

Expected output
> Max: 100
> Min: 7
"""

numbers = [18, 32, 72, 100, 7, 74, 17, 45, 42, 66, 86, 79, 23, 54, 35]
minimum = numbers[0]
maximum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

print("Max: " + str(maximum))
print("Min: " + str(minimum))
