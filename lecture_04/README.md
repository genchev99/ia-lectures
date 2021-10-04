# Introduction to programing with Python️ - Part 4

We are going to solve the problems from the last time and also a couple of new ones.

## Table of contents 📜

- [Exercise](#exercise)
- [Google FooBar Challenge](#-google-foobar-challenges)

## Exercise

### Problem 01

`Sum` of a list. Given this list of numbers:

```python
numbers = [80, 23, 78, 56, 14, 73, 4, 46, 79, 9, 55, 84, 65, 20, 27]
```

Write a python program that will calculate their `sum`.

###### Expected output

> 713

---

### Problem 02

`Average` of a list. Given this list of numbers:

```python
numbers = [3, 56, 97, 43, 25, 72, 74, 40, 82, 84, 24, 51, 28, 87, 81]
```

Write a python program that will calculate the `average (mean)`.

###### Expected output

> 56.46666666666667

---

### Problem 03

`Min` and `Max` in a list. Given this list of numbers:

```python
numbers = [18, 32, 72, 100, 7, 74, 17, 45, 42, 66, 86, 79, 23, 54, 35]
```

Write a python program that will find the `max` and `min` numbers in that list.

###### Expected output

> Max: 100
>
> Min: 7

---

### Problem 04

Find the `second biggest` number. Given this list of numbers:

```python
numbers = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
```

Write a python program that will find the `second biggest` number in that list.

###### Expected output

> 82

---

### Problem 05

Find if list contains a `given` numbers. Given this list of numbers, and a number to look for:

```python
numbers = [68, 65, 30, 87, 21, 17, 96, 70, 64, 34, 14, 90, 86, 31, 29, 40, 59, 23, 25, 95, 60, 85, 42, 37, 57, 18, 27,
           77, 36, 75, 4, 5, 38, 63, 76, 81, 53, 24, 62, 98, 83, 55, 67, 1, 7, 92, 8, 51, 52, 61, 3, 56, 97, 12, 71, 20,
           16, 26, 50, 10, 73, 89, 88, 49, 28, 100, 13, 47, 69]
number = 42
```

Write a python program that will print: `Number found` if the `number` is in the `numbers` list. Otherwise,
print: `Not found...`

###### Expected output

> Number found

---

### Problem 06

Find if a list has `duplicated` numbers. Given these lists of numbers:

```python
numbers_01 = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
numbers_02 = [89, 75, 78, 84, 27, 82, 63, 72, 6, 41, 77, 35, 92, 90, 8, 72, 21, 74, 48, 97, 42, 28, 45, 84, 22, 63, 4,
              74, 6, 70, 13, 30]
numbers_03 = [54, 32, 37, 35, 66, 48, 15, 27, 48, 82, 38, 96, 58, 95, 13, 64, 67, 58, 94, 90, 10, 11, 36, 29, 36, 25,
              20, 94, 25, 74, 42, 30, 74, 52, 12, 39, 70, 30, 14, 91, 92, 55, 11, 6, 55, 36, 92, 84, 11, 90, 76, 11, 18,
              32, 1, 16, 73, 66, 21, 86, 49, 53, 33, 25]
numbers_04 = [68, 65, 30, 87, 21, 17, 96, 70, 64, 34, 14, 90, 86, 31, 29, 40, 59, 23, 25, 95, 60, 85, 42, 37, 57, 18,
              27, 77, 36, 75, 4, 5, 38, 63, 76, 81, 53, 24, 62, 98, 83, 55, 67, 1, 7, 92, 8, 51, 52, 61, 3, 56, 97, 12,
              71, 20, 16, 26, 50, 10, 73, 89, 88, 49, 28, 100, 13, 47, 15]
```

Write a python program that will print: `Duplicates found` for each of these lists if any of the numbers can be found
twice or more in the same list. Otherwise, print: `The list is free of duplicates`

###### Expected output

> List #1: The list is free of duplicates
>
> List #2: The list is free of duplicates
>
> List #3: Duplicates found
>
> List #4: The list is free of duplicates

---

### Problem 07

Find if a string contains a `character`. Given this `string` and the `character` to look for:

```python
string = "the quick brown fox jumps over the lazy dog"
character = "q"
```

Write a python program that will print: `Character found` if the `character` is in the `string`. Otherwise,
print: `Not found...`

###### Expected output

> Character found

---

### Problem 08

Find if a string contains a `substring`. Given this `string` and the `substring` to look for:

```python
string = "the quick brown fox jumps over the lazy dog"
substring = "brown fox"
```

Write a python program that will print: `Substring found` if the `substring` is in the prime `string`. Otherwise,
print: `Not found...`

###### Expected output

> Substring found

---

### Problem 09

Check for `Balanced Brackets` in a `string`
> example for balanced : "(b * b) - (4 * a * c)"
>
> example for not balanced : "b) * b)"

```python
string_01 = "Thi(s is) (a very annoy)ing ((se(n)tence)) with some (brackets)"
string_02 = "This i(s a v)ery ann)oy(ing sentence w((i)th so)me (b(r(a(c(k(e(t(s))))))))"
```

Write a python program that will print for each strings (01 and 02): `Balanced brackets` if the brackets in the string
are well-balanced. Otherwise, print: `Not balanced brackets`.

###### Expected output

> String #1: Balanced brackets
>
> String #2: Not balanced brackets

---

### Problem 10

`Reverse` the list. Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Write a python program that will print the list in reversed order.

###### Expected output

> [6, 5, 4, 3, 2, 1]

---

### Problem 11

Write a Python program to insert a new item before the `second` element in an existing array. Given this list of
numbers:

```python
numbers = [1, 2, 3, 4, 5, 6]
number_to_insert = 42
```

###### Expected output

> [1, 42, 2, 3, 4, 5, 6]
---

### Problem 12

Write a Python program to remove a specified item using the index from an array. Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 5, 6]
index_to_remove = 3
```

###### Expected output

> [1, 2, 3, 5, 6]

---

### Problem 13

Write a Python program to remove the `first occurrence of a specified element` from an array. Given this list of
numbers:

```python
numbers = [1, 2, 3, 4, 5, 3, 6, 3]
number_to_remove = 3
```

###### Expected output

> [1, 2, 4, 5, 3, 6, 3]


---

### Problem 14

Write a Python program to find a pair (print the product) with `the highest product` from a given array of integers.
Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 7, 0, 8, 4]
```

###### Expected output

> 56 # 7 * 8

---

### Problem 15

Bubble sort. Given this list of numbers:

```python
numbers = [1, 2, 3, 4, 7, 0, 8, 4]
```

###### Expected output

> [0, 1, 2, 3, 4, 4, 7, 8]
---

### Problem 15

Write a program that reads from the console an integer n and draws a rectangle with size n with two asterisks is its
center as in the examples below.

#### Sample input and output

###### Input #1

> 2

###### Output #1

```
%%%%
%**%
%%%%
```

###### Input #2

> 3

###### Output #2

```
%%%%%%
%    %
% ** %
%    %
%%%%%%
```

###### Input #3

> 4

###### Output #3

```
%%%%%%%%
%      %
%  **  %
%      %
%%%%%%%%
```

###### Input #4

> 5

###### Output #4

```
%%%%%%%%%%
%        %
%        %
%   **   %
%        %
%        %
%%%%%%%%%%
```

## ⭐ Google FooBar challenges

### Problem 01

Who would’ve guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP’s quantum
antimatter reactor core with solar arrays, and you’ve been tasked with setting up the solar panels.

Due to the nature of the space station’s outer paneling, all of its solar panels must be squares. Fortunately, you have
one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(
TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square
yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3
square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar
panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make
out of those panels, starting with the largest squares first. So, following the example above, solution(12) would
return [9, 1, 1, 1].

```
Input:
solution.solution(15324)
Output:
15129,169,25,1

Input:
solution.solution(12)
Output:
9,1,1,1
```

---

### Problem 02

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to
say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier
sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of
the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and
414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a
limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can
be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as
the solution. L will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, but each
element in the list may only be used once.

```
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311
Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
```
