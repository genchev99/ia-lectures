class Egg:
    def __init__(self, egg_id: str, size: float):
        self.id = egg_id
        self.size = size


class Basket:
    def __init__(self):
        self.eggs = []

    def __getitem__(self, item):
        return item


if __name__ == '__main__':
    basket = Basket()
    print(basket[2])
    print(basket["egg_id_123"])
