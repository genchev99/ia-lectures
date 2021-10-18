class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def display(self):
        print("x: " + str(self.x) + " y: " + str(self.y))


class Circle:
    def __init__(self, radius: float, center: Point):
        self.radius = radius
        self.center = center

    def area(self) -> float:
        return 3.14 * (self.radius ** 2)

    def perimeter(self) -> float:
        return 3.14 * self.radius

    def distance(self, p: Point):
        a = self.center.x - p.x
        b = self.center.y - p.y

        return (a ** 2 + b ** 2) ** 0.5

    def position(self, p: Point):
        dis = self.distance(p)

        if dis < self.radius:
            return 1
        elif dis == self.radius:
            return 0
        else:
            return -1


# 2 3 5 7 1
center_point = Point(2.0, 3.0)
center_point.display()
