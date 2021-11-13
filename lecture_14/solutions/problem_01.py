class MyPositiveInteger:
    def __init__(self, val: int):
        self.value = val

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, new_value: int):
        if new_value >= 0:
            self.__value = new_value
        else:
            self.__value = -new_value

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, MyPositiveInteger):
            return self.value + other.value
        else:
            raise Exception("Not of type MyPositiveInteger")

    def __sub__(self, other):
        if isinstance(other, MyPositiveInteger):
            return abs(self.value - other.value)
        else:
            raise Exception("Not of type MyPositiveInteger")

    def __isub__(self, other):
        if isinstance(other, MyPositiveInteger):
            self.value = abs(self.value - other.value)
            return self
        else:
            raise Exception("Not of type MyPositiveInteger")


if __name__ == '__main__':
    print(MyPositiveInteger(10) - MyPositiveInteger(17))  # >>> 7

    print(MyPositiveInteger(-14) - MyPositiveInteger(100))

    p = MyPositiveInteger(20)
    print(p)
    p -= MyPositiveInteger(10)
    print(p)
    print(type(p))
