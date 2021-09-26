"""
Given a floating point number `d` from the standard input perform the following conditional operations:

- if the number is greater or equal than `5.50` and less or equal than `6.00` print: `Отличен`
- if the number is greater or equal than `4.50` and less than `5.50` print: `Мн. Добър`
- if the number is greater or equal than `3.50` and less than `4.50` print: `Добър`
- if the number is greater or equal than `3.00` and less than `3.50` print: `Среден`
- if the number is greater or equal than `2.00` and less than `3.00` print: `Слаб`
- otherwise, print: `Error - the provided number is invalid`

Input format
> A single line containing decimal number (d)

Simple input
> 5.47

Simple output
> Мн. Добър
"""

d = float(input("Input number: "))

if 6.0 >= d >= 5.5:
    print("Отличен")
elif 5.5 > d >= 4.5:
    print("Мн. Добър")
elif 4.5 > d >= 3.5:
    print("Добър")
elif 3.5 > d >= 3.0:
    print("Среден")
elif 3.0 > d >= 2.0:
    print("Слаб")
else:
    print("Error - the provided number is invalid")
