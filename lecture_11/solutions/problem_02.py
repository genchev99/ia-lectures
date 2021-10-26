class Shape(object):
    def area(self):
        raise NotImplementedError()

    def perimeter(self):
        raise NotImplementedError()

    def __str__(self):
        return type(self).__name__


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    shapes = [Square(10), Circle(20), Rectangle(3.4, 1.5)]

    for shape in shapes:
        print(f"shape: {type(shape)}, area: {shape.area()}, perimeter: {shape.perimeter()}")
