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

    def display(self):
        print(self.values)

def smallest_in_queue(queue: Queue):
    if queue.empty():
        raise Exception("The queue is empty")
    
    helper_smallest = queue.head()
    helper_queue = Queue()

    while queue.empty() is False:
        temp = queue.dequeue()
        if temp < helper_smallest:
            helper_smallest = temp
        
        helper_queue.enqueue(temp)
    
    while helper_queue.empty() is False:
        temp = helper_queue.dequeue()

        if temp != helper_smallest:
            queue.enqueue(temp)

    return queue

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(10)
    queue.display()
    queue = smallest_in_queue(queue)
    queue.display()
