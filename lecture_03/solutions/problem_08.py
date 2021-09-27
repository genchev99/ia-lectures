"""
Find if a string contains a `substring`. Given this `string` and the `substring` to look for:
```python
string = "the quick brown fox jumps over the lazy dog"
substring = "brown fox"
```
Write a python program that will print: `Substring found` if the `substring` is in the prime `string`. Otherwise,
print: `Not found...`

Expected output
> Substring found
"""

string = "the quick brown fox jumps over the lazy dog"
substring = "brown fox"
found = False

for i in range(len(string) - len(substring) + 1):
    miss_match = False
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            miss_match = True

    if miss_match is False:
        found = True

if found:
    print("Substring found")
else:
    print("Not found...")
