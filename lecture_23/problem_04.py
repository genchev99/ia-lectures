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


def is_valid_expression(expression: str) -> bool:
    stack = Stack()

    for char in expression:
        if char == "[" or char == "{" or char == "(":
            # This code can be simplified to -> if char in ["{", "(", "["]:
            stack.push(char)

        # The following code can be wrapped in a function and you can call it 3 times for all 3 types of brackets
        # BUT for simplicity I'll leave it like that
        if char == ")":
            if stack.empty() or stack.top() != "(":
                return False
            stack.pop()
        if char == "]":
            if stack.empty() or stack.top() != "[":
                return False
            stack.pop()
        if char == "}":
            if stack.empty() or stack.top() != "{":
                return False
            stack.pop()

    # The next lines can be simplified to return stack.empty()
    # but I'll leave them like that so it's easier to read
    if stack.empty() is True:
        return True

    return False


if __name__ == "__main__":
    print(is_valid_expression("(asd[a]{123})"))
    print(is_valid_expression("(asd[a]{123)"))
    print(is_valid_expression("(asd[a]123})"))
    print(is_valid_expression("(asd[a123})"))
    print(is_valid_expression(")(asd[a]{123})"))
