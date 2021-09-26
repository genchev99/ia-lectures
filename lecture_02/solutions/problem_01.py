"""
Given an integer `n` from the standard input perform the following conditional operations:

- if the number is `odd` print on the standard output: `The number is odd`
- otherwise, print: `The number is even`

Input format:
> A single line containing positive integer (n)

Simple input:
> 2

Simple output:
> The number is even
"""

n = int(input("Input number: "))

if n % 2 != 0:
    print("The number is odd")
else:
    print("The number is even")
