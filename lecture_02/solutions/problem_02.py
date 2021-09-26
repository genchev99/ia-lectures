"""
Given two integers `x` and `y` from the standard input perform the following conditional operations:

- if `x` is greater than `y` print: `X is greater than Y`
- if `x` is less than `y` print: `X is less than Y`
- if `x` is equal to `y` print: `X is equal to Y`

Input format:
> Two lines containing two positive integers (x and y)

Simple input:
> 16
> 32

Simple output:
> X is less than Y

"""

x = int(input("First number (x): "))
y = int(input("Second number (y): "))

if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is equal to Y")
