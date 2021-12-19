def validate(string: str):
    s = Stack()

    for char in string:
        if char == "(":
            s.push(char)

        if char == ")":
            if s.empty():
                return False
            
            if s.top() == "(":
                s.pop()

    return s.empty()
