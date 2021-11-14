# Working with files in Python

## Table of contents 📜

- [The `with open(...) as ...` context manager](#the-with-open-as--context-manager)

## The `with open(...) as ...` context manager

In Python working with files is made really easy throughout the `with open(...)` construction (Note that this is a
wrapper that helps to write cleaner code). In other lower level languages when you open a file either for reading or
writing you need to control the file, so you don't accidentally leave hanging file descriptors after the need for them
is over 😒 (the `with open(...)` will manage this for us). For our needs we won't dig too deep in how working with files
is managed by the OS. We'll only focus on how to work with files in python and get it as a given (black box).

To read the contents of file in Python you need to use the following syntax:

```python
with open("data.txt", "r") as fd:
    data = fd.read()
```

As you can see the function `open()` takes two arguments. The first argument is the path (a string | a path-like object)
to the file we want to open and the second argument is the `mode` in which the file will be opened.

Here is a list of the `modes` and their description (from python docs)

|Character | Description |
|----------|-------------|
|`'r'`     | open for reading (default)|
|`'w'`     | open for writing, truncating the file first|
|`'x'`     | open for exclusive creation, failing if the file already exists|
|`'a'`     | open for writing, appending to the end of file if it exists|
|`'b'`     | binary mode|
|`'t'`     | text mode (default)|
|`'+'`     | open for updating (reading and writing)|

The default mode is `'r'` (open for reading text, a synonym of `'rt'`).

Based on this if we want to open a file for writing the code will look like:

```python
with open('data.txt', 'w') as fd:
    data = 'some data to be written to the file'
    fd.write(data)
```

In both cases `open()` returns a `file descriptor` (file handler) which has some special methods and behaviour.

The `file descriptor` (file handler) has the following methods (not all of them just the ones that we are going to need.
If you need you can find the full list [here](https://www.w3schools.com/python/python_ref_file.asp)):

|Method |Description |
|-------|------------|
|`read()` | Returns the file content |
|`readline()` | Returns one line from the file |
|`readlines()` | Returns a `list` of lines from the file |
|`seek()` | Changes the file seeker position |
|`write()` | Writes a passed string to the file |
|`writelines()` | Writes a list of string to the file |
|`close()` | Closes the file (we won't need to manage that) |
|`flush()` | Forces the OS to flush all the data from the internal buffer |

You can have a combination of these methods and functions to form a program that has meaningful purpose and saves you
some time. For example the "program" below takes a `word` and a `file_path` and checks if the file contains that word.

```python
def is_word_in_file(word: str, file_path: str):
    with open(file_path, "r") as fh:
        for line in fh.readlines():
            if word in line:
                return True

    return False


word = input("Input word to search for: ")
file_path = input("Input a file path to search in: ")
result = is_word_in_file(word, file_path)

if result:
    print("The word was found in the file")
else:
    print("The word was NOT found in the file")
```

This example can be further more expanded. For example instead of just checking for one word passed from the standard
input we can have a file that has stored words that we are going to check for 😉.

```python
def file_contains_any_keywords(keywords_path: str, search_path: str):
    with open(search_path, "r") as search_fh, open(keywords_path, "r") as keywords_fh:
        for keyword in keywords_fh.readlines():
            # Note that this time we directly use read instead of reading line by line
            if keyword in search_fh.read():
                return True

    return False


keywords_file_path = input("Input a file path to the keywords file: ")
search_in_file_path = input("Input a file path to search in: ")
result = file_contains_any_keywords(keywords_file_path, search_in_file_path)

if result:
    print("At least one keyword was found in the file")
else:
    print("NONE keywords were found in the file")
```

## Problem 01

Implement a simpler version of the shell command `cat` in python.

The `cat` command prints the contents of a file to the terminal (in our case this will be the standard output).

1. Make the program work with one file provided from the standard input.
2. Make the program work with arbitrary number if files all provided from the standard input.

```python
# Hint
while True:
    file_path = input("Enter a file path: ")
    if not file_path:
        break
    # do something with file
```

## Problem 02

Implement a simpler version of the shell command `tee` in python.

The `tee` commands takes 0 or more files as arguments and starts reading from the standard input. For every file that it
reads it's writing it to the standard output and also to the files.

Make the program work with arbitrary number if files all provided from the standard input (reuse the hint).

## Problem 03

Implement a simpler version of the shell command `grep` in python.

The `grep` commands takes a `keyword` and 1 or more `files` and returns the lines from the files that contain the word.

For our implementation we'll support the arbitrary amount of files to work with (one or
more) [again we can use the approach from problem 01] and will read the `keyword` from the standard input (before the
files). After that for each line that contains the keyword we will print
`"file_name:line_number:line_content"` where the `file_name` is the name of the file where the keyword was
found, `line_number` is the line number where the word was found and `line_content` is the full content of line (not
just the word).

## Problem 04

Implement a simpler version of the shell command `sort` in python.

The `sort` command takes a file and returns its contents in alphabetical sorted order.

Our program will take two files from the standard input. The first file will contain the unsorted file (source_file) and
the second one will be the file name where we'll store the sorted file contents (destination_file). It's very important
`NOT TO` overwrite any existing data on your computer so make sure to use a proper mode that will ensure that there is
no existing file with the same name (take a loNOT TOok at the table).

## Problem 05 - Problem 04 from the shared file with tasks

Hint - to check if a file exists you can use

```python
import os.path

os.path.isfile(file_name) 
```
