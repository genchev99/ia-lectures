"""
Write a python function that returns the unique numbers from a list of numbers. Write a python program that uses the
function with these arguments and prints the result for each of them.

```python
list_of_numbers = [1, 6, 4, 9, 5, 9, 10, 1, 7, 5, 7, 7, 10, 9, 2, 9, 4, 3, 7, 9]
list_of_numbers = [16, 0, -35, -27, -24, 31, 32, -15, 34, 18, 14, 12, -1, -10, -16, 43, 6, 0, -5, -9, -23, 24, -16, 48,
                   40, 45, 5, 0, 37, 8, 39, 49, -4, 34, 2, 2, 40, 28, -50, 21]
```

```python
def is_unique(list_of_numbers: list, number: int) -> bool:
    pass


def unique_all(list_of_numbers: list) -> list:
    pass
```

Expected output
> [1, 2, 3, 4, 5, 6, 7, 9, 10]
> [0, 2, 5, 6, 8, 12, 14, 16, 18, 21, 24, 28, 31, 32, 34, 37, 39, 40, 43, 45, 48, 49, -50, -35, -27, -24, -23, -16, -15, -10, -9, -5, -4, -1]
"""


def is_unique(list_of_numbers: list, number: int) -> bool:
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if i != j and list_of_numbers[i] == list_of_numbers[j]:
                return False

    return True


def unique_all(list_of_numbers: list) -> list:
    unique = []

    for number in list_of_numbers:
        if is_unique(list_of_numbers, number):
            unique.append(number)

    return unique


print(unique_all([1, 2, 3, 4, 5, 6, 7, 9, 10]))
print(unique_all(
    [0, 2, 5, 6, 8, 12, 14, 16, 18, 21, 24, 28, 31, 32, 34, 37, 39, 40, 43, 45, 48, 49, -50, -35, -27, -24, -23, -16,
     -15, -10, -9, -5, -4, -1]))
