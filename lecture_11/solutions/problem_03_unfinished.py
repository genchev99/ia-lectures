class Bike:
    def __init__(self, price):
        self.price = price
        self.days_since_last_service = 0

    def age(self, age_with=1):
        self.days_since_last_service += age_with

    def service_cost(self):
        return self.days_since_last_service * 7

    def service(self):
        self.days_since_last_service = 0

    def sell(self):
        return self.price - self.days_since_last_service * 10

    def is_running(self):
        if self.days_since_last_service <= 10:
            return True

        return False


class Garage:
    def __init__(self, budget):
        self.bikes = []
        self.budget = budget

    def buy_new_bike(self, bike: Bike):
        if self.budget >= bike.price:
            self.bikes.append(bike)
            self.budget -= bike.price

    def payday(self, salary):
        self.budget += salary

    def pass_a_day(self):
        for bike in self.bikes:
            bike.age(1)

    def service_all_bikes(self):
        pass

    def is_any_bike_running(self):
        for bike in self.bikes:
            if bike.is_running():
                return True

        return False
