"""
Find if a list has `duplicated` numbers. Given these lists of numbers:
```python
numbers_01 = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
numbers_02 = [89, 75, 78, 84, 27, 82, 63, 72, 6, 41, 77, 35, 92, 90, 8, 72, 21, 74, 48, 97, 42, 28, 45, 84, 22, 63, 4,
              74, 6, 70, 13, 30]
numbers_03 = [54, 32, 37, 35, 66, 48, 15, 27, 48, 82, 38, 96, 58, 95, 13, 64, 67, 58, 94, 90, 10, 11, 36, 29, 36, 25,
              20, 94, 25, 74, 42, 30, 74, 52, 12, 39, 70, 30, 14, 91, 92, 55, 11, 6, 55, 36, 92, 84, 11, 90, 76, 11, 18,
              32, 1, 16, 73, 66, 21, 86, 49, 53, 33, 25]
numbers_04 = [68, 65, 30, 87, 21, 17, 96, 70, 64, 34, 14, 90, 86, 31, 29, 40, 59, 23, 25, 95, 60, 85, 42, 37, 57, 18,
              27, 77, 36, 75, 4, 5, 38, 63, 76, 81, 53, 24, 62, 98, 83, 55, 67, 1, 7, 92, 8, 51, 52, 61, 3, 56, 97, 12,
              71, 20, 16, 26, 50, 10, 73, 89, 88, 49, 28, 100, 13, 47, 15]
```

Write a python program that will print: `Duplicates found` for each of these lists if any of the numbers can be found
twice or more in the same list. Otherwise, print: `The list is free of duplicates`

Expected output
> List #1: The list is free of duplicates
> List #2: The list is free of duplicates
> List #3: Duplicates found
> List #4: The list is free of duplicates
"""

numbers = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]

# !IMPORTANT NOTE!: this is a solution only for the first list of numbers - the rest should be similar
length = len(numbers)
duplicates = False
for i in range(length):
    for j in range(length):
        if i != j and numbers[i] == numbers[j]:
            duplicates = True

if duplicates:
    print("Duplicates found")
else:
    print("The list is free of duplicates")
