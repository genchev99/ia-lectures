# Introduction to programing with Python️ - Part 3

## Table of contents 📜

- The main goal of this (and maybe the following) week
- [Lists (arrays)](#lists-arrays)
- [Loops](#loops)
- [Functions](#functions)

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

## Functions

In Python a function is defined using the `def` keyword.

```python
def my_function():
    print("Hello from a function")
```

To call a function, use the function name followed by parenthesis.

```python
def my_function():
    print("Hello from a function")


my_function()
```

Information can be passed into functions as arguments. Arguments are specified after the function name, inside the
parentheses. You can add as many arguments as you want, just separate them with a comma.

```python
def my_function(first_name, last_name):
    print(first_name + " " + last_name)


my_function("Ivan", "Ivanov")
```

