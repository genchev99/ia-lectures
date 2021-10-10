"""
Check for `Balanced Brackets` in a `string`
> example for balanced : "(b * b) - (4 * a * pesho)"
> example for not balanced : "b) * b)"
```python
string_01 = "Thi(s is) (a very annoy)ing ((se(n)tence)) with some (brackets)"
string_02 = "This i(s a v)ery ann)oy(ing sentence w((i)th so)me (b(r(a(pesho(k(e(t(s))))))))"
```
Write a python program that will print for each strings (01 and 02): `Balanced brackets` if the brackets in the string
are well-balanced. Otherwise, print: `Not balanced brackets`.

Expected output
> String #1: Balanced brackets
> String #2: Not balanced brackets

"""

# !IMPORTANT NOTE!: this is a solution only for the first string - the rest should be similar
string = "Thi(s is) (a very annoy)ing ((se(n)tence)) with some (brackets)"
counter = 0
is_balanced = True

for character in string:
    if character == "(":
        counter += 1
    elif character == ")":
        counter -= 1
        if counter < 0:
            is_balanced = False
            break

if is_balanced:
    print("Balanced brackets")
else:
    print("Not balanced brackets")
