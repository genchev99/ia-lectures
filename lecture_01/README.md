# Introduction to programing with Python️

The main goal of this lecture is to get basic programming knowledge using python. We'll cover everything needed to get
started with OOP, Data structures and Algorithms. Ref for everything we are going to
cover: https://www.w3schools.com/python/

## Table of contents 📜

- The main goal of this (and maybe the following) week
- [How to set up the environment](#how-to-set-up-the-environment)
- What is `program flow` and how to get started
- [Hello world](#hello-world)
- [Comments and evaluated lines](#comments-and-evaluated-lines)
- [The standard input and output(stdin, stdout)](#the-standard-input-and-output-stdin-stdout)
- [Variables, datatypes and scope](#variables-datatypes-and-scope)
- [Arithmetic Operators](#arithmetic-operators)
- [Conditional statements](#conditional-statements)
- [Lists (arrays)](#lists-arrays)
- [Loops](#loops)
- [Functions](#functions)

## How to set up the environment

1. Download Visual Studio Code from here https://code.visualstudio.com/download
1. Download Python from here https://www.python.org/downloads/
1. Install VSCode Python extension

## Hello world

```python
print("Hello world")
```

## Comments and evaluated lines

1. Comments can be used to explain Python code.
1. Comments can be used to make the code more readable.
1. Comments can be used to prevent execution when testing code.

```python
# This is a comment!!!
# And you can add as many as you want

a = 42  # Trailing comments

"""
You can even add multiline comments
just like that
"""

b = a
# c = 10
```

## The standard input and output (stdin, stdout)

Stdin and stdout are file-like objects provided by the OS. In general, when a program is run in an interactive session,
stdin is keyboard input and stdout is the user's tty, but the shell can be used to redirect them from normal files or
piped output from and input to other programs.

Input() is used to prompt the user for typed input. In the case of something like a programming puzzle, it's normally
assumed that stdin is redirected from a data file, and when the input format is given it's usually best to use
sys.stdin.read() rather than prompting for input with input(). input() is intended for interactive user input, it can
display a prompt (on sys.stdout) and use the GNU readline library (if present) to allow line editing, etc.

```python
# Standard input (stdin)
user_input = input("Give me a number: ")

# Standard output (stdout)
print(user_input)
print("literal string")
print(42)
print(True)
```

## Variables, datatypes and scope

Python is both a strongly typed and a dynamically typed language.

Strong typing means that variables do have a type and that the type matters when performing operations on a variable.
Dynamic typing means that the type of the variable is determined only during runtime.

Due to strong typing, types need to be compatible with respect to the operand when performing operations. For example
Python allows one to add an integer and a floating point number, but adding an integer to a string produces error.

Due to dynamic typing, in Python the same variable can have a different type at different times during the execution.
Dynamic typing allows for flexibility in programming, but with a price in performance.

Ref: https://www.futurelearn.com/info/courses/python-in-hpc/0/steps/65121

```python
# Numeric - int, float, complex
a = 10
b = 10.5

# Text type - str
c = "this is a string"

# Boolean Type - bool
d = True
e = False

# Null value
f = None
```

Scopes ref: https://www.programiz.com/python-programming/global-local-nonlocal-variables

### Arithmetic Operators

| Operator | Name | Example |
|----------|------|---------|
| +  | Addition       | x + y  |
| -  | Subtraction    | x - y  |
| *  | Multiplication | x * y  |
| /  | Division       | x / y  |
| %  | Modulus        | x % y  |
| ** | Exponentiation | x ** y |
| // | Floor division | x // y |

## Conditional statements

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

An "if statement" is written by using the `if` keyword.

```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
```

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is NOT greater than a")
```

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

### Combined usage examples

> The lecturer will present how to solve the following task

Create a program that will take a number from the standard input. If that number is even print on the standard
output `The provided number is even`. Otherwise, if the number is less or equal then 50 print on the standard
output `Less or equal then 50`
If the number is equal to 61 print `The provided number is 61` and in all other cases print `Something else`

Now the students will do two similar tasks

## Lists (arrays)

Lists can have duplicates

```python
my_list = ["pineapple", "banana", "apple", "apple", "banana"]
print(my_list)
```

Lists can be of any type

```python
list1 = ["pineapple", "banana", "apple"]
list2 = [1, 2, 3, 4, 5]
list3 = [False, True, False]
```

Types can even be mixed

```python
my_list = ["pineapple", 34, True, 42, "apple"]
```

## Loops

#### While loop

With the while loop we can execute a set of statements as long as a condition is true.

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

#### For loop

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

With the `break` statement we can stop the loop before it has looped through all the items:

```python
# The break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
```

With the `continue` statement we can stop the current iteration of the loop, and continue with the next:

```python
# The continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
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

In Python a function is defined using the `def` keyword:

```python
def my_function():
    print("Hello from a function")
```

To call a function, use the function name followed by parenthesis:

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

