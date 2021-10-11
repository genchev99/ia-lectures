"""
Write a python function that returns the sum of list. Write a python program that uses the function with these arguments
and prints the result for each of them.
```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [55, 96, 59, 84, 19, 70, 1, 39, 74, 93, 75, 41, 91, 39, 82, 88, 83, 12, 19, 40]
l = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
```
```python
def my_sum(l: list) -> int:
    pass
```

Expected output
> 55
> 1160
> 146
"""


def my_sum(l: list) -> int:
    s = 0
    for n in l:
        s += n

    return s


print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(my_sum([55, 96, 59, 84, 19, 70, 1, 39, 74, 93, 75, 41, 91, 39, 82, 88, 83, 12, 19, 40]))
print(my_sum([-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]))
