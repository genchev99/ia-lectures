class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


rectangle = Rectangle(20.0, 5.0)
print(rectangle.length)
print(rectangle.width)
print(rectangle.area())
