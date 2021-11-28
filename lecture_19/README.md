# Data structures in Python - Part 1

## Table of contents 📜

- [Linked list](#linked-list)

## Linked list

![-](https://miro.medium.com/max/970/0*JnRHkVYr5Dw0nqcx.png)

A linked list is a sequence of data elements, which are connected together via links. Each data element contains a
connection to another data element in form of a pointer. Python does not have linked lists in its standard library. We
implement the concept of linked lists using the concept of nodes.

Operations:

- `create()` — creates a new empty linked list
- `empty()` — checks if the list is empty
- `insert(x, p)` — adds the element `x` at position `t`
- `delete(p)` — removes an element from a given position `p`
- `get(p)` — returns the element on a given piston `p`

#### The node concept!

![-](https://cdn.programiz.com/sites/tutorial2program/files/full-binary-tree_0.png)

The `node` is a simple class that serves the purpose of data wrapper which can point to other (different) `node`

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


a = Node(5)
b = Node(7)
a.next = b
b.prev = a
```

### Singly-likened list

![-](https://media.geeksforgeeks.org/wp-content/uploads/singly-linkedlist.png)

`Singly linked lists` contain nodes which have a data field as well as `next` field, which points to the next node in
line of nodes.

```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"({self.data})"


class SinglyLinkedList:
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


if __name__ == '__main__':
    s = SinglyLinkedList()
    s.append(Node(10))
    s.append(Node(20))
    s.append(Node(30))
    s.append(Node(40))
    s.append(Node(50))
    print(s)
    s.insert(Node(100), 2)
    s.insert(Node(666), 0)
    print(s)
    s.delete(3)
    print(s)
    s.delete(0)
    print(s)
```

### Circular singly linked list

![-](https://i0.wp.com/algorithms.tutorialhorizon.com/files/2016/03/Circular-Linked-List.png)

> Open question: which operations we need to change to make our SinglyLinkedList into CircularSinglyLinkedList?

## Problem 01

Append `SinglyLinkedList` `A` at the end of list `B`.

> Approach #1: append each element from list #2 at the end of list #1
>
> Approach #2: point the last node from list #1 to the head of #2

## Problem 02

Reverse the elements of a `SinglyLinkedList`

> Approach #1: Move each consecutive node after the first element to the beginning
>
> Approach #2: Move in-place using the references

###### Input: Head of following linked list

> 1->2->3->4->NULL

###### Output: Linked list should be changed to,

> 4->3->2->1->NULL

###### Input: Head of following linked list

> 1->2->3->4->5->NULL

###### Output: Linked list should be changed to,

> 5->4->3->2->1->NULL

## Doubly Linked list

![-](https://miro.medium.com/max/2000/1*Rkn3q6HJoEkRO4T_SVlyuw.png)

> Open question: what do we need to change to make our SinglyLinkedList implementation into DoublyLinkedList?

## Circular Doubly Linked list

![-](https://www.alphacodingskills.com/imgfiles/circular-doubly-linked-list.PNG)

> Open question: what do we need to change to make our DoublyLinkedList implementation into CircularDoublyLinkedList?

## Problem 03

Implement a circular singly-linked list in Python

## Problem 04

Implement a doubly-linked list in Python

## Problem 05

Check if a doubly-linked list is a palindrome
