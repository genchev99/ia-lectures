"""
Write a Python program to find a pair (print the product) with `the highest product` from a given array of integers.
Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 7, 0, 8, 4]
```

Expected output
> 56 # 7 * 8
"""

# The "easier" way - with nested loops

numbers = [1, 2, 3, 4, 7, 0, 8, 4]
biggest_product = numbers[0] * numbers[1]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] * numbers[j] > biggest_product:
            biggest_product = numbers[i] * numbers[j]

print(biggest_product)

# The second way is to find the biggest, the second biggest, the smallest and the second smallest
# and to get max(biggest * second_biggest, smallest * second_smallest)
