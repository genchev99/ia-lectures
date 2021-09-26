"""
Given two integers `x` and `y` from the standard input perform the following arithmetic operations:

- Print the sum of `x` and `y`
- Print the difference of `x` and `y`
- Print the product of `x` and `y`
- Print if `x` is dividable by `y`
- Print if `y` is dividable by `x`
- Print the square of `x`
- Print `x` to the power of `y`

Input format
> Two lines containing two integers (x and y)

Simple input
> 9
> 3

Simple output
> 12
> 6
> 27
> True
> False
> 81
> 729
"""

x = int(input("First number (x): "))
y = int(input("Second number (y): "))

print(x + y)
print(x - y)
print(x * y)
print(bool(x % y))
print(bool(y % x))
print(x * x)  # print(x ** 2)
print(x ** y)
