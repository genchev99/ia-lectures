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

    def __str__(self):
        return str(self.values)


def is_letter(char: str) -> bool:
    if len(char) != 1:
        return False

    return char.islower()


def is_special_char(char: str) -> bool:
    return is_letter(char) or char == "?"


def is_valid(expression: str) -> bool:
    stack = Stack()

    for char in expression:
        if char == "(":
            if stack.empty() or not is_letter(stack.top()):
                return False

            stack.push(char)
        elif is_letter(char):
            if not stack.empty() and stack.top() != "(":
                return False

            stack.push(char)
        elif char == ",":
            if stack.empty() or not is_special_char(stack.top()):
                return False

            stack.pop()

            if stack.empty() or stack.top() != "(":
                return False
        elif char == ")":
            if stack.empty() or not is_special_char(stack.top()):
                return False

            stack.pop()

            if stack.empty() or stack.top() != "(":
                return False

            stack.pop()

            if stack.empty() or not is_letter(stack.top()):
                return False

            stack.pop()
            stack.push("?")
        else:
            # Every other case
            return False

    if stack.empty() or not is_special_char(stack.top()):
        return False

    stack.pop()

    if stack.empty() is True:
        return True

    return False


def valid_test(expression: str):
    print(expression, is_valid(expression))


if __name__ == '__main__':
    valid_test("a")
    valid_test("b")
    valid_test("a(b)")
    valid_test("a(b,c)")
    valid_test("a(b,c(d))")

    valid_test("a,b")
    valid_test("()")
    valid_test("(,)")
