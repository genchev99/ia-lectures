"""
We'll call a number (integer) `weird` if:

- the number is `even`
- the number is in the inclusive range of `16` to `32`
- the number is in the inclusive range of `64` to `128`
- the number is `dividable` by `5`

Given an integer `n` from the standard input print `Weird` if it's (`n`) weird. Otherwise, print `Not Weird`.

Input format
> A single line containing positive integer (n)

Simple input
> 17

Simple output
> Weird
"""

number = int(input("Input number: "))

if number % 2 == 0 or (number >= 16 and number <= 32) or (64 <= number <= 128) or number % 5 == 0:
    print("Weird")
else:
    print("Not Weird")
