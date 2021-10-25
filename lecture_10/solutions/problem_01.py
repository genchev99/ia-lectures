"""
- Implement a class `Vehicle` with properties `listing_id`, (unique identification number), `price`, `max_speed` (
  maximum possible speed), `number_of_seats` and `year_of_creation`. Also, add these 2 methods `print_vehicle_type()` -
  that prints `Base Vehicle` and `listing_information() -> str` that returns the listing information of the vehicle as a
  string (will be used later on for the listing of the different vehicles)
- Implement a class `Bicycle` that extends `Vehicle` and adds `make` (which is the brand of the bicycle)
  and `is_mountain` (which is true if the bike is a mountain bike) to the properties and override
  the `print_vehicle_type()` method to make it print `Bicycle`. Also, override the other method to return a proper
  listing string (do that for all vehicle types).
- Implement a class `Engine` with properties `fuel_type` (diesel or petrol) and `engine_size` (the size of the engine in
  cubic centimeters)
- Implement a class `MotorVehicle` that extends `Vehicle` and `Engine` and adds properties `is_accident_free`
  and `weight`. Override the `print_vehicle_type()` method to print `Motor Vehicle`
- Implement a class `Car` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the car), `airbags` and `mileage`. Override the `print_vehicle_type()` method to print `Car`
- Implement a class `Motorcycle` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the motorcycle), `is_sport_bike` and `mileage`. Override the `print_vehicle_type()` method to
  print `Motorcycle`
- Implement a class `Boat` that extends `MotorVehicle` and adds the properties `make` (tha brand of the vehicle)
  , `model` (the model of the boat) and `mileage`. Override the `print_vehicle_type()` method to print `Boat`

Implement a class `AutomobileShop` that has a list of available vehicles to purchase. The class has the following
methods too:

- `list_vehicles()` - that prints all available vehicles
- `add_vehicle(vehicle: Vehicle)` - adds a new vehicle to the list
- `remove_vehicle(id)` - removes vehicle by id
- `sort_by_price()` - sorts the list by price

1. Create a new instance of `AutomobileShop`
1. Add a couple of new vehicles to the shop (more than one of each type) using the `add_vehicle` method
1. List the available vehicles
1. Remove a vehicle (which simulates a sale) and list the vehicles again
1. Sort the list of available vehicles by and list them again
"""


class Vehicle:
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation):
        self.listing_id = listing_id
        self.price = price
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats
        self.year_of_creation = year_of_creation

    def print_vehicle_type(self):
        print("Base Vehicle")

    def listing_information(self) -> str:
        return str(self.listing_id) + " " + str(self.price) + " " + str(self.year_of_creation) + " " + str(self.max_speed) + " " + str(self.number_of_seats)


class Bicycle(Vehicle):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, make, is_mountain):
        super(Bicycle, self).__init__(listing_id, price, max_speed, number_of_seats, year_of_creation)
        self.make = make
        self.is_mountain = is_mountain

    def print_vehicle_type(self):
        print("Bicycle")

    def listing_information(self) -> str:
        return str(self.listing_id) + " " + str(self.price) + " " + self.make + " " + str(self.year_of_creation) + " " + str(self.max_speed) + " " + str(self.number_of_seats) + " " + str(self.is_mountain)


class Engine:
    def __init__(self, fuel_type, engine_size):
        self.fuel_type = fuel_type
        self.engine_size = engine_size


class MotorVehicle(Vehicle, Engine):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight):
        Vehicle.__init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation)
        Engine.__init__(self, fuel_type, engine_size)

        self.is_accident_free = is_accident_free
        self.weight = weight

    def print_vehicle_type(self):
        print("Motor Vehicle")

    def listing_information(self) -> str:
        return f"{self.listing_id} {self.price} {self.year_of_creation} {self.fuel_type} {self.engine_size} {self.is_accident_free} {self.weight} {self.max_speed} {self.year_of_creation}"


class Car(MotorVehicle):
    pass


class Motorcycle(MotorVehicle):
    pass


class Boat(MotorVehicle):
    pass


class AutomobileShop:
    items = []

    def list_vehicles(self):
        pass

    def add_vehicle(self, vehicle: Vehicle):
        pass

    def remove_vehicle(self, id_number: int):
        pass

    def sort_by_price(self):
        pass
