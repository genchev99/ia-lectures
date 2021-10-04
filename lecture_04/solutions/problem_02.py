"""

`Average` of a list. Given this list of numbers:
```python
numbers = [3, 56, 97, 43, 25, 72, 74, 40, 82, 84, 24, 51, 28, 87, 81]
```
Write a python program that will calculate the `average (mean)`.

Expected output
> 56.46666666666667
"""

s = 0
numbers = [3, 56, 97, 43, 25, 72, 74, 40, 82, 84, 24, 51, 28, 87, 81]

for number in numbers:
    s += number

average = s / len(numbers)
print(average)
