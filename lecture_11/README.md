# OOP with Python️

## Table of contents 📜

- [Exercise on Inheritance](#exercise-on-inheritance)

## Exercise on Inheritance

## Problem 01

#### The bank account wallet problem

Create a new class `PersonIdentification` with the following attributes:

- `first_name` - the first name of the person
- `last_name` - the last name of the person
- `id_number` - the id number if the person [EGN]

> It takes all if them as arguments in the constructor

Create a new class `BankAccountWallet` with the following attributes:

- `owner: PersonIdentification` - the owner of the wallet - he is of type `PersonIdentification`
- `balance: float` - the money balance in the wallet
- `accountIdentificator` - a number that uniquely identifies the account - can be autoincremented
  using `Class attributes`
    - https://dzone.com/articles/python-class-attributes-vs-instance-attributes

It defines and implements the following methods too:

- `deposit()` - adds money to the balance
- `widthdraw()` - removes money from the balance if enough
- `print_balance()` - prints the balance in this format `balance: {balance}`

1. Create a new instance of `BankAccountWallet`
1. Deposit money to it (1000 dollars)
1. Print the balance
1. Withdraw money from it (755.3)
1. Print the balance

## Problem 02

1. Create a base class `Shape` that defines two methods:

- `area()` - returns the area of the shape
- `perimeter()` - returns the perimeter of the shape

> Note: for the base class you can leave them blank (use the keyword pass)
> Remember this class because next time we'll use it to define abstract classes

2. Create a new class `Circle` that extends `Shape` and takes one new parameter in the constructor - `radius`. Override
   both methods [`area` and `perimeter`] to calculate the values properly for circle.

3. Create a new class `Rectangle` that extends `Shape` and takes two new parameters in the constructor - `width`
   , `length`. Override both methods [`area` and `perimeter`] to calculate the values properly for rectangle.

3. Create a new class `Square` that extends `Rectangle` and takes one new parameter in the constructor - `length`. Think
   of a way how to reuse the definitions of `Rectangle` without having to override the methods.

## Problem 03

1. Create a class `Bike` that takes one parameter in the constructor - `price`. It defines a
   property `days_since_last_service`. It also defines the following methods:

- `age(age_with=1)` - makes the bike become older - adds `age_with` (which defaults to `1`) to `days_since_last_service`
- `service_cost()` - the amount of money needed to service the bike `days_since_last_service * 7`
- `service()` - restores the bike 'as new' - sets `days_since_last_service` to `0`.
- `sell()` - sells the bike for `price - days_since_last_service * 10`
- `is_running()` - returns `True` if the bike has been serviced in the past `10` days.

2. Create a class `Garage` which will hold some `Bikes`. It will have a property `bikes` which will be a list of `Bikes`
   and another property `budget` which will be used to service and buy bew bikes. It will also implement the following
   methods:

- `buy_new_bike(bike: Bike)` - buys a new bike and adds it to the garage (this operation costs money - verify if you
  have them).
- `payday(salary: float)` - Congrats! You got your salary - add it to your budget.
- `pass_a_day()` - a new day has passed - age all your bikes with `1` day
- `service_all_bikes()` - services all your bikes
- `service_all_bikes_older_than(older_than: int)` - services all bikes older than given amount of days
- `sell_a_bike(index: int)` - sells a bike by a given index - adds money to your budget
- `is_any_bike_running()` - returns true if any of your bikes is running
- `print_bikes()` - prints your bikes

1. Create a new instance of `Garage` with `1000` dollars of init budget.
1. Buy a new bike for `700` dollars
1. A day has passed!
1. Print your bikes
1. Buy a new bike for `250` dollars
1. A day has passed!
1. Print your bikes
1. Try to buy a new bike for `400` dollars
1. A day has passed!
1. Print your bikes
1. A day has passed!
1. Is any of your bikes running?
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. A day has passed!
1. Is any of your bikes running?
1. Congrats - it's time for salary you got `2000`
1. Service all your bikes
1. Is any of your bikes running?

## Problem 04

!Note: the classes design is not a strict as possible. It's for educational purposes.

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