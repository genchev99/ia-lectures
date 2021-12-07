def iterative_fib(n: int): 
    if n == 0:
        return 0

    index = 1
    prev = 0
    curr = 1

    while index != n:
        temp = prev + curr
        prev = curr
        curr = temp
        index += 1

    
    return curr


def recursive_fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return recursive_fib(n - 1) + recursive_fib(n - 2)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, x: int, y: int) -> None:
        self.head = None

        if x > y:
            return
        
        self.head = Node(x)
        current = self.head
        index = x + 1
        while index <= y:
            current.next = Node(index)
            current = current.next
            index += 1

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = node

    def count(self, x: int):
        counter = 0

        current = self.head
        while current is not None:
            if current.data == x:
                counter += 1
            
            current = current.next
        
        return counter
    
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, " -> ", end="")
            current = current.next


if __name__ == "__main__":
    ll = LinkedList(10, 15)
    # ll.append(Node(10))
    # ll.append(Node(20))
    # ll.append(Node(10))
    # ll.append(Node(10))
    # ll.append(Node(30))
    ll.display()
    # print()
    # print(ll.count(10))
