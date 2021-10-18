class MyMath:
    def pow(self, x: float, n: float):
        return x ** n

    def factorial(self, x: int):
        f = 1

        for number in range(1, x + 1):
            f *= number

        return f

    def floor(self, x: float):
        return int(x)

    def difference(self, a: float, b: float):
        return a - b


m = MyMath()
print(m.factorial(5))  # 120
print(m.floor(5.3))  # 5
print(m.pow(2, 10))  # 1024
print(m.difference(10, 6))  # 4
