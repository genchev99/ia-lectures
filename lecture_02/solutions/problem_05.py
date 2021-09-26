"""
Given an integers `n` from the standard input that represents a year find if it's `Leap` or not. If it's `leap`
print: `Leap year`, otherwise print: `Common year`

Wikipedia states `leap` year as a special year containing one extra day i.e. total `366 days` in a year. A year is said
to be `leap` year, if the year is exactly `divisible by 4 but and not divisible by 100`. Year is also a `leap` year if
it is exactly `divisible by 400`.

Input format
> A single line containing positive integer (n)

Simple input
> 2004

Simple output
> Leap year
"""

year = int(input("Input year: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Common year")
