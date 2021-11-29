# Data structures in Python - Part 2 - Exercise

### Singly linked list implementation

```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"({self.data})"


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.length = 0

    def empty(self):
        return self.head is None

    def append(self, node: Node):
        if self.head is None:
            # We don't have leading element yet
            self.head = node
        else:
            self.get(self.length - 1).next = node

        self.length += 1

    def insert(self, node: Node, p: int):
        if p == 0:
            node.next = self.head
            self.head = node
            return

        prev = self.get(p - 1)
        node.next = prev.next
        prev.next = node
        self.length += 1

    def delete(self, p: int):
        if p == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head

        prev = self.get(p - 1)
        to_remove = prev.next
        prev.next = to_remove.next
        to_remove.next = None

    def get(self, p: int) -> Node:
        current = self.head

        for _ in range(p):
            current = current.next

        return current

    def __str__(self):
        res = ""
        current = self.head
        while current is not None:
            res += f"{current} -> "
            current = current.next

        return res
```

## Problem 01

Extend the functionality of our LinkedList with the following methods

- `is_incremental()` - returns `True` if for every two items `x` and `y` (where `x` is before `y` in order) the
  following statement `x < y` is `True`. Otherwise, it returns `False`.
- `fill_gaps()` - If the list is incremental this method should fill all missing numbers between two consecutive
  nodes `x` and `y` (where `y - x > 1`). The end goal is to have a list that contains all numbers (integers) in tha
  range `[head, tail]`

> Example: [1, 4, 6] -> [1, 2, 3, 4, 5, 6]

## Problem 02

Extend the functionality of our LinkedList with the following methods

- `remove_idx()` - removes all elements that are equal to the absolute value of the difference between their index and
  the index of the last element. All `x` in our list `where x = abs(indexOf(x) - len(list))`

> Example: [1] -> [1]
>
> Example: [0] -> []
>
> Example: [2, 1, 0] -> []
>
> Example: [11, 6, 12, 4, 3, 13, 1, 0] -> [11, 12, 13]

## Problem 03

Extend the functionality of our LinkedList with the following methods

- `mirror()` - appends (at the end of the list) all elements of the list but in reversed order.

> Example: [1, 2, 3] -> [1, 2, 3, 3, 2, 1]

## Problem 04

Extend the functionality of our LinkedList with the following methods

- `is_gradually_incremental()` - returns `True` if for every two items `x` and `y` (where `x` is before `y` in order)
  the following statement `x <= y` is `True`. Otherwise, it returns `False`.
- `remove_dups` - checks if the list `is_gradually_incremental` and if so removes all duplicates until it
  becomes `incremental`

> Example: [1, 2, 2, 2, 2, 3, 7] -> [1, 2, 3, 7]

# Problem 05 and 06 are for homework!!!!!!!

## Problem 05

Extend the functionality of our LinkedList with the following methods

- `remove_sub(other: LinkedList)` - deletes all sublists from `self` where they are equal (as values and order)
  to `other`.

> Example: self = [1, 2, 3, 4, 5, 6], other = [6] -> [1, 2, 3, 4, 5]
>
> Example: self = [1, 2, 3, 4, 5, 6], other = [2] -> [1, 3, 4, 5, 6]
>
> Example: self = [1, 2, 3, 2, 3, 4, 2, 3], other = [2, 3] -> [1, 4]

## Problem 06

Extend the functionality of our LinkedList with the following methods

- `dup_sub(k: int)` - returns `True` if the list contains `2 different` substrings with length of `k` (positive integer)
  . Otherwise, it returns `False`.

# Problem 05 and 06 are for homework!!!!!!!