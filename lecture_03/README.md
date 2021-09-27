# Introduction to programing with Python️ - Part 3

## Table of contents 📜

- The main goal of this (and maybe the following) week
- [Lists (arrays)](#lists-_arrays_)
- [Loops](#loops)

## Lists (_arrays_)

`Lists` are used to store `multiple items` in a `single` variable.

`Lists` are created using `square brackets`.

```python
my_list = ["pesho", "gosho", "ivan"]
```

### List items data types

`Lists` can be of any type

```python
list1 = ["pesho", "gosho", "ivan"]
list2 = [1, 2, 3, 4, 5]
list3 = [False, True, False]
```

Types can even be `mixed`

```python
my_list = ["pesho", 34, True, 42, "gosho"]
```

### List semantics and access

`List items` are ordered, changeable, and allow duplicate values.

`List items` are `indexed`, the first item has index `[0]`, the second item has index `[1]` etc.

```python
my_list = ["pesho", "gosho", "ivan", 42]
first_item = my_list[0]
second_item = my_list[1]
third_item = my_list[2]

# You can count backwards - starting from the last item
last_item = my_list[-1]
```

`List items` are changeable

```python
my_list = ["pesho", "gosho", "ivan", 42]

my_list[1] = "ralica"
print(my_list)  # >>> ['pesho', 'ralica', 'ivan', 42]
```

### List length

All `lists` have length - to determine how many items a list has, use the `len()` function.

```python
my_list = []  # an empty list
print(len(my_list))  # >>> 0

my_list = ["pesho", "gosho", "ivan", 42]
print(len(my_list))  # >>> 4
```

### Insert new items

To `insert` a new list item, without replacing any of the existing values, we can use the `insert()` method.

The `insert()` method inserts an item at the specified index.

```python
my_list = ["pesho", "gosho", "ivan"]
my_list.insert(2, "ralica")
print(my_list)  # >>> ['pesho', 'gosho', 'ralica', 'ivan']
```

To `add` a new list item to the end of the list you can use the `append()` method.

```python
my_list = ["pesho", "gosho", "ivan"]
my_list.append(10)
print(my_list)  # >>> ['pesho', 'gosho', 'ivan', 10]
```

### Remove items

The `pop()` method removes the specified index.

```python
my_list = ["pesho", "gosho", "ivan"]
my_list.pop(1)
print(my_list)  # >>> ['pesho', 'ivan']
```

The `pop()` method without an argument will remove the last item

```python
my_list = ["pesho", "gosho", "ivan"]
my_list.pop()
print(my_list)  # >>> ['pesho', 'gosho']
```

## Loops

### While loop

With the `while loop` we can execute a set of statements as long as a condition is `True`.

```python
i = 1
while i < 6:
    print(i)
    i += 1  # same as `i = i + 1`
```

The loop can be `‘stuck’` in so-called `endless loop` if the condition is always `True`.

```python
i = 1
while True:
    print(i)
    i += 1  # same as `i = i + 1`
```

#### Break and continue

With the `break` statement we can `stop the loop even if the while condition is true`.

```python
i = 1
while i < 6:
    if i == 4:
        # when i becomes equal to 4 then loop will exit
        break

    print(i)
    i += 1  # same as `i = i + 1`
```

With the `continue` statement we can stop the current iteration, and `continue` with the `next`.

```python
i = 1
while i < 6:
    if i % 2:
        # when i is even the loop will continue with the next iteration
        continue

    print(i)
    i += 1  # same as `i = i + 1`
```

We can loop through `lists`

```python
my_list = ["pesho", "gosho", "ivan"]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1  # same as `i = i + 1`
```

### For loop

A `for loop` is used for iterating over a `sequence` (that is either a `list`, a tuple, a dictionary, a set, or a
string).

```python
my_list = ["pesho", "gosho", "ivan"]
for name in my_list:
    print(name)
```

With the `break` statement we can stop the loop before it has looped through all the items.

```python
my_list = ["pesho", "gosho", "ivan"]
for name in my_list:
    if name == "gosho":
        break

    print(name)
```

With the `continue` statement we can stop the current iteration of the loop, and continue with the next.

```python
my_list = ["pesho", "gosho", "ivan"]
for name in my_list:
    if name == "gosho":
        continue

    print(name)
```

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and
stops before a specified number.

```python
range(10)
# range(start, stop, step)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

To loop through a set of code a specified number of times, we can use the `range()` function

```python
for x in range(10):
    print(x)
```

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
