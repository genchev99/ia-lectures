# Introduction to programing with Python️ - Part 2

## Table of contents 📜

- Revision of variables, datatypes, stdin, stdout, comments, arithmetic operators and conditional statements
- [Exercises](#exercises)

## Exercises

#### Problem 01

Given an integer `n` from the standard input perform the following conditional operations:

- if the number is `odd` print on the standard output: `The number is odd`
- otherwise, print: `The number is even`

###### Input format

> A single line containing positive integer (n)

###### Simple input

> 2

###### Simple output

> The number is even


---

#### Problem 02

Given two integers `x` and `y` from the standard input perform the following conditional operations:

- if `x` is greater than `y` print: `X is greater than Y`
- if `x` is less than `y` print: `X is less than Y`
- if `x` is equal to `y` print: `X is equal to Y`

###### Input format

> Two lines containing two positive integers (x and y)

###### Simple input

> 16
>
> 32

###### Simple output

> X is less than Y

---

#### Problem 03

Given two integers `x` and `y` from the standard input and the max number between them.

###### Input format

> Two lines containing two integers (x and y)

###### Simple input

> 16
>
> 32

###### Simple output

> 32

---

#### Problem 04

Given three integers `x`, `y` and `z` from the standard input find the minimum number between them.

###### Input format

> Three lines containing integers (x, y and z)

###### Simple input

> 16
>
> 32
>
> 64

###### Simple output

> 16

---

#### Problem 05

Given an integers `n` from the standard input that represents a year find if it's `Leap` or not. If it's `leap`
print: `Leap year`, otherwise print: `Common year`

Wikipedia states `leap` year as a special year containing one extra day i.e. total `366 days` in a year. A year is said
to be `leap` year, if the year is exactly `divisible by 4 but and not divisible by 100`. Year is also a `leap` year if
it is exactly `divisible by 400`.

###### Input format

> A single line containing positive integer (n)

###### Simple input

> 2004

###### Simple output

> Leap year

---

#### Problem 06

We'll call a number (integer) `weird` if:

- the number is `even`
- the number is in the inclusive range of `16` to `32`
- the number is in the inclusive range of `64` to `128`
- the number is `dividable` by `5`

Given an integer `n` from the standard input print `Weird` if it's (`n`) weird. Otherwise, print `Not Weird`.

###### Input format

> A single line containing positive integer (n)

###### Simple input

> 17

###### Simple output

> Weird

---

#### Problem 07

Given a floating point number `d` from the standard input perform the following conditional operations:

- if the number is greater or equal than `5.50` and less or equal than `6.00` print: `Отличен`
- if the number is greater or equal than `4.50` and less than `5.50` print: `Мн. Добър`
- if the number is greater or equal than `3.50` and less than `4.50` print: `Добър`
- if the number is greater or equal than `3.00` and less than `3.50` print: `Среден`
- if the number is greater or equal than `2.00` and less than `3.00` print: `Слаб`
- otherwise, print: `Error - the provided number is invalid`

###### Input format

> A single line containing decimal number (d)

###### Simple input

> 5.47

###### Simple output

> Мн. Добър
---

#### Problem 08

Given two integers `x` and `y` from the standard input perform the following arithmetic operations:

- Print the sum of `x` and `y`
- Print the difference of `x` and `y`
- Print the product of `x` and `y`
- Print if `x` is dividable by `y`
- Print if `y` is dividable by `x`
- Print the square of `x`
- Print `x` to the power of `y`

###### Input format

> Two lines containing two integers (x and y)

###### Simple input

> 9
>
> 3

###### Simple output

> 12
>
> 6
>
> 27
>
> True
>
> False
>
> 81
>
> 729

---

#### Problem 09

Find all `roots` of a `quadratic equation`. Given three integers `a`, `b` and `c` from the standard input calculate
the `discriminant` and find the roots.

###### Input format

> Three lines containing integers (x, y and z)

###### Simple input

> 8
>
> -4
>
> -2

###### Simple output

> Root #1: 0.80
>
> Root #2: -0.30
