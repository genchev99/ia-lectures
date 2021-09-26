"""
Given three integers `x`, `y` and `z` from the standard input find the minimum number between them.

Input format
> Three lines containing integers (x, y and z)

Simple input
> 16
> 32
> 64

Simple output
> 16
"""

x = int(input("First number (x): "))
y = int(input("Second number (y): "))
z = int(input("Third number (z): "))

if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
else:
    print(z)
