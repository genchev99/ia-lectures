"""
Given two integers `x` and `y` from the standard input and the max number between them.

Input format:
> Two lines containing two integers (x and y)

Simple input:
> 16
> 32

Simple output:
> 32
"""

x = int(input("First number (x): "))
y = int(input("Second number (y): "))

if x > y:
    print(x)
else:
    print(y)
