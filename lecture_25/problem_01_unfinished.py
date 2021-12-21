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

class Board:
    def __init__(self, x, y, n) -> None:
        self.size = 20
        self.santa = set()

        self.x = x
        self.y = y
        self.n = n

    def reversed_row(self, original_row: int) -> int:
        return self.size - original_row - 1

    def display(self):
        for y in range(self.size):
            print(str(y).zfill(3), end="")
            for x in range(self.size):
                if x == self.x and self.reversed_row(y) == self.y:
                    # Prints the init position
                    print("$ ", end="")
                elif (x, self.reversed_row(y)) in self.santa:
                    print("S ", end="")
                else:
                    print("_ ", end="")
            
            print()
        
        for x in range(self.size):
            print (f"{x} ", end="")
    
    def run(self):
        # Adds the init position to the set
        q_last = Queue()
        q_last.enqueue((self.x, self.y))
        self.santa.add((self.x, self.y))

        for _ in range(self.n):
            q = Queue()
            
            while not q_last.empty():
                current = q_last.dequeue()
                x, y = current

                q.enqueue((x+2, y+1))
                q.enqueue((x+2, y-1))
                q.enqueue((x-2, y+1))
                q.enqueue((x-2, y-1))
                q.enqueue((x+1, y+2))
                q.enqueue((x-1, y+2))
                q.enqueue((x+1, y-2))
                q.enqueue((x-1, y-2))
            
            while not q.empty():
                current = q.dequeue()
                self.santa.add(current)

                q_last.enqueue(current)

            


if __name__ == "__main__":
    x = 10
    y = 10
    n = 12

    board = Board(x, y, n)
    board.run()
    board.display()
