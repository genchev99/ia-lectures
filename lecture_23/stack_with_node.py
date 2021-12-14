from _typeshed import Self


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, n: Node):
        self.length += 1

        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def pop(self):
        if self.empty():
            raise Exception("Cannot pop from empty stack")

        self.length -= 1

        temp = self.head
        self.head = self.head.next

        return temp

    def empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def top(self):
        return self.head
