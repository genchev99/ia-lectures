class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * (self.radius ** 2)

    def perimeter(self) -> float:
        return 3.14 * self.radius


circle = Circle(10.0)
print(circle.area())
print(circle.perimeter())
