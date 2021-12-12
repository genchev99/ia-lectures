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
    # def __init__(self, x: int, y: int) -> None:
    #     self.head = None

    #     if x > y:
    #         return
        
    #     self.head = Node(x)
    #     current = self.head
    #     index = x + 1
    #     while index <= y:
    #         current.next = Node(index)
    #         current = current.next
    #         index += 1

    def __init__(self) -> None:
        self.head = None

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
    
    def remove_all(self, x: int):
        current = self.head

        while current.next is not None:
            if current.next.data == x:
                current.next = (current.next).next
            else:
                current = current.next

        if self.head is not None and self.head.data == x:
            self.head = self.head.next

    def map(self, f):
        current = self.head

        while current is not None:
            current.data = f(current.data)
            current = current.next
    
    def filter(self, f):
        current = self.head

        while current is not None:
            if f(current.data) is False:
                # Remove the element
                pass

            current = current.next

def suc(x):
    return x + 1

def pow3(x):
    return x ** 3

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(10))
    ll.append(Node(10))
    ll.append(Node(30))
    ll.display()
    print()
    # ll.remove_all(10)
    ll.map(pow3)
    ll.display()
    # print()
    # print(ll.count(10))
