class Stack:
    def __init__(self):
        self.values = []

    def empty(self) -> bool:
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def top(self):
        if self.empty():
            raise Exception("The stack is empty")

        return self.values[-1]

    def push(self, val):
        self.values.append(val)

    def pop(self):
        last = self.top()
        self.values.pop()
        
        return last

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.top())
    s.pop()
    print(s.top())
