"""
Create a class Person with `first_name` and `last_name`. Create a new `@property blood_type (str)` for that class and a
setter. Inside that setter make sure that the only allowed blood types are ["A", "B", "AB", "0"]. In case the value is
something else make sure to throw a proper exception!

Create a method `print_person_info()` which prints the person information in the following
format `"{first_name} {last_name} - {blood_type}"`

Create a new `Person` with each type of blood and print each of them.

Create one with blood type `"AO"` - it should throw an error.
"""


class Person:
    def __init__(self, first_name: str, last_name: str, blood_type: str):
        self.first_name = first_name
        self.last_name = last_name
        self.blood_type = blood_type

    @property
    def blood_type(self):
        return self.__blood_type

    @blood_type.setter
    def blood_type(self, new_blood_type: str):
        allowed_blood_types = ["A", "B", "AB", "0"]

        if new_blood_type not in allowed_blood_types:
            raise ValueError("Invalid blood type")

        self.__blood_type = new_blood_type

    def print_person_information(self):
        print(f"{self.first_name} {self.last_name} - {self.blood_type}")


if __name__ == "__main__":
    people = [
        Person("Ivan", "Ivanov", "A"),
        Person("Petar", "Petrov", "B"),
        Person("Dimitar", "Dimitrov", "AB"),
        Person("Martin", "Martinov", "0"),
    ]

    for person in people:
        person.print_person_information()

    Person("Gosho", "Goshev", "BB")
