class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, x):
        self.values.append(x)

    def dequeue(self):
        if self.empty():
            raise Exception("Cannot dequeue elements from empty queue")

        return self.values.pop(0)

    def head(self):
        return self.values[0]

    def rear(self):
        return self.values[-1]

    def empty(self) -> bool:
        return len(self.values) == 0
