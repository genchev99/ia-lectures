"""
`Sum` of a list. Given this list of numbers:
```python
numbers = [80, 23, 78, 56, 14, 73, 4, 46, 79, 9, 55, 84, 65, 20, 27]
```
Write a python program that will calculate their `sum`.

Expected output
> 713
"""

s = 0
numbers = [80, 23, 78, 56, 14, 73, 4, 46, 79, 9, 55, 84, 65, 20, 27]

for number in numbers:
    s = s + number  # same as s += number

print(s)
