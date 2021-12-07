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
        self.length += 1
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = node

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

    def remove_idx(self):
        last_index = self.length - 1
        current_index = 0

        while self.head is not None and self.head.data == last_index:
            self.head = self.head.next
            last_index -= 1

        current = self.head
        while current is not None and current.next is not None:
            if current.next.data == last_index - (current_index + 1):
                current.next = current.next.next
                last_index -= 1
            else:
                current_index += 1
                current = current.next

    def mirror(self):
        last = self.get(self.length - 1)
        curr = self.head

        for _ in range(self.length):
            last.next = Node(curr.data, last.next)
            curr = curr.next
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    
    print(ll)
    ll.mirror()
    print(ll)
