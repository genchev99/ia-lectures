class CarRegistryRecord:
    def __init__(self, owner_name: str, register_car_number: int, car_unique_id: int):
        self.owner_name = owner_name
        self.register_car_number = register_car_number

        self.car_unique_id = car_unique_id


class CarRegistry:
    def __init__(self):
        self.registered_cars = []
        self.catalog = Catalog()

    def add_new_registered_car(self, registration: CarRegistryRecord):
        for registered_car in self.registered_cars:
            if registration.register_car_number == registered_car.register_car_number:
                print("There is already a car with the same registration")
                return

        self.registered_cars.append(registration)

    def car_ownership_count_by_id(self, id: int):
        counter = 0
        for registered_car in self.registered_cars:
            if registered_car.car_unique_id == id:
                counter += 1

        return counter

    def average_power(self):
        sum_power = 0

        if len(self.registered_cars) == 0:
            return 0

        for r in self.registered_cars:
            car = self.catalog.get_car_by_id(r.car_unique_id)
            sum_power += car.power

        return sum_power / len(self.registered_cars)

    def report(self):
        id_0_car_count = self.car_ownership_count_by_id(0)
        id_1_car_count = self.car_ownership_count_by_id(1)
        id_2_car_count = self.car_ownership_count_by_id(2)
        id_3_car_count = self.car_ownership_count_by_id(3)

        all_cars = [id_0_car_count, id_1_car_count, id_2_car_count, id_3_car_count]
        max_count = max(all_cars)
        most_popular = None

        if max_count == id_0_car_count:
            most_popular = self.catalog.get_car_by_id(0)
        elif max_count == id_1_car_count:
            most_popular = self.catalog.get_car_by_id(1)
        elif max_count == id_2_car_count:
            most_popular = self.catalog.get_car_by_id(2)
        elif max_count == id_3_car_count:
            most_popular = self.catalog.get_car_by_id(3)

        average_power = self.average_power()

        with open("car-report.txt", "w") as fd:
            fd.write(str(most_popular))
            fd.write("  average power: ")
            fd.write(str(average_power))


class Car:
    id_generator = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power

        self.id = self.id_generator
        Car.id_generator += 1

    def __str__(self) -> str:
        return f"{self.id}:{self.name}:{self.power}"


class Catalog:
    def __init__(self):
        self.cars = [
            Car("Lambordgini Murcielago", 670),
            Car("Mercedes-AMG", 503),
            Car("Pagani Zonda R", 740),
            Car("Bugatti Veyron", 1020),
        ]

    def get_car_by_id(self, id: int):
        for car in self.cars:
            if car.id == id:
                return car


if __name__ == '__main__':
    # catalog = Catalog()
    # print(catalog.get_car_by_id(2))
    car_registry = CarRegistry()
    car_registry.add_new_registered_car(CarRegistryRecord("Pesho", 1234, 0))
    car_registry.add_new_registered_car(CarRegistryRecord("Pesho", 2222, 3))
    car_registry.add_new_registered_car(CarRegistryRecord("Ivan", 2222, 2))
    car_registry.report()
