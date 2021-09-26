"""
Find all `roots` of a `quadratic equation`. Given three integers `a`, `b` and `c` from the standard input calculate
the `discriminant` and find the roots.

Input format
> Three lines containing integers (x, y and z)

Simple input
> 8
> -4
> -2

Simple output
> Root #1: 0.80
> Root #2: -0.30
"""
import math

a = int(input("Input number (a): "))
b = int(input("Input number (b): "))
c = int(input("Input number (c): "))

discriminant = b ** 2 - 4 * a * c
root_01 = None
root_02 = None

if discriminant >= 0:
    root_01 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_02 = (-b - math.sqrt(discriminant)) / (2 * a)

print("Root #1: " + format(root_01, '.2f'))
print("Root #2: " + format(root_02, '.2f'))
