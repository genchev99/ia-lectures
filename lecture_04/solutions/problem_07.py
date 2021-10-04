"""
Find if a string contains a `character`. Given this `string` and the `character` to look for:
```python
string = "the quick brown fox jumps over the lazy dog"
character = "q"
```
Write a python program that will print: `Character found` if the `character` is in the `string`. Otherwise,
print: `Not found...`

Expected output
> Character found
"""

string = "the quick brown fox jumps over the lazy dog"
character = "q"
found = False

for char in string:
    if char == character:
        found = True

if found:
    print("Character found")
else:
    print("Not found...")
