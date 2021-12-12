## Stack

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end and an element is removed from that end only. The insert and delete
operations are often called push and pop.

![stack](https://atechdaily.com/resources/images/posts/2020/5/431/stack-operations-in-c.gif)

![stack](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/stack.png)

Interface:

- `empty()` – Returns whether the stack is empty – Time Complexity: `O(1)`
- `size()` – Returns the size of the stack – Time Complexity: O`(1)`
- `top()` – Returns a reference to the topmost element of the stack – Time Complexity: `O(1)`
- `push(a)` – Inserts the element ‘a’ at the top of the stack – Time Complexity: `O(1)`
- `pop()` – Deletes the topmost element of the stack – Time Complexity: `O(1)`

### Implementation

You can implement a `stack` in many ways. You can even use the built-in collections for this purpose. For our needs
we'll implement a `stack` in two ways - using a `list` and using our own implementation of `Node` and connections (like
we did for linked lists).

### TODO - implement a `stack` using `list`

```python
class Stack:
    def __init__(self):
        self.values = []

    def empty(self) -> bool:
        pass

    def size(self):
        pass

    def top(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass
```

### Problems

#### Problem 01

Implement a method `display()` that will print tha stack on the standard output using the following format. If the stack
has these elements `[2, 4, 5, 6]` the output should look like:

> | 6 |
>
> | 5 |
>
> | 4 |
>
> | 2 |
>
> ===

#### Problem 02

Да се напише метода `sum`, която сумира всички елементи в стека и резултата бива записан обратно в стека.

#### Problem 03

Даден е израз, който може да съдържа отварящи и затварящи скоби. Да се напише функция, която проверява дали скобите на
израза са правилно балансирани. Например, изразът `(x+(y+(1+2)))` считаме за правилно балансиран, но не и
израза `(x+y)*3)+(x+(1+2)`.

#### Problem 04

Да се реши горната задача при положение, че изразът може да има едновременно кръгли, фигурни и квадратни скоби.

#### Problem 05

Да се имплементира `stack` посредством `Node`-ове

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Queue

Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the
least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the
consumer that came first is served first.

![queue](https://i1.faceprep.in/Companies-1/queue-operations.gif)

![queue](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)

interface:

- `enqueue(x)` - adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time
  Complexity : `O(1)`
- `dequeue()` - removes an item from the queue. The items are popped in the same order in which they are pushed. If the
  queue is empty, then it is said to be an Underflow condition – Time Complexity : `O(1)`
- `head()` - get the front item from queue – Time Complexity : `O(1)`
- `rear()` - get the last item from queue – Time Complexity : `O(1)`
- `empty()` - returns true if the queue is empty

### Implementation

You can implement a `queue` in many ways. You can even use the built-in collections for this purpose. For our needs
we'll implement a `queue` in two ways - using a `list` and using our own implementation of `Node` and connections (like
we did for linked lists).

### TODO - implement a `queue` using `list`

```python
class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, x):
        pass

    def dequeue(self):
        pass

    def head(self):
        pass

    def rear(self):
        pass

    def empty(self) -> bool:
        pass
```

#### Problem 01

Дадена е опашка q. Да се изключи от q най-малкият и`елемент, като всички останали елементи останат в опашката (не
непременно в първоначалния ред)

#### Problem 02

Казваме, че `k` е число на Hamming, ако простите делители на `k` са сред `2`, `3`, и `5`, т.е. `k=2^x*3^y*5^z`
за `x, y, z >= 0`

Да се изведат в нарастващ ред всички числа на Hamming, които са по-малки от `n`.
(Направете функция `first_hamming(n)`, която да връща лист опашка от първите n числа)

#### Problem 03

Да се имплементира `queue` посредством `Node`-ове

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

#### Problem 04

#### TODO: да бъде оправено условие

Да се реализира задача за ход на коня (ще бъде разяснено по време на час)