"""
Write a python function that returns the maximum number between three arguments. Write a python program that uses the
function with these arguments and prints the result for each.

1. x=10, y=20, z=30
1. x=12, y=-42, z=8
1. x=5, y=72, z=-7
1. x=`result from (1)`, y=`result from (2)`, z=`result from (3)`

```python
def maximum(x: int, y: int, z: int) -> int:
    pass
```
Expected output
> 30
> 12
> 72
> 72
"""


def maximum(x: int, y: int, z: int) -> int:
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


max_01 = maximum(x=10, y=20, z=30)
max_02 = maximum(x=12, y=-42, z=8)
max_03 = maximum(x=5, y=72, z=-7)

print(max_01)
print(max_02)
print(max_03)
print(maximum(max_01, max_02, max_03))
