"""
Write a python function that takes a string as an argument and returns `True` if it is `palindrome` and `False` if not.
Write a python program that uses the function with these arguments and prints the result for each of them.

> Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

```python
string = "pesho"
string = "peshohsep"
string = "123321"
string = "shopenpesho"
```

```python
def is_palindrome(string: str) -> bool:
    pass
```

Expected output
> False
> True
> True
> False
"""


def is_palindrome(string: str) -> bool:
    for i in range(int(len(string) / 2)):
        if string[i] != string[-i - 1]:
            return False

    return True


print(is_palindrome("pesho"))
print(is_palindrome("peshohsep"))
print(is_palindrome("123321"))
print(is_palindrome("shopenpesho"))
