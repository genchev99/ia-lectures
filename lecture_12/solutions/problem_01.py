"""
Create a class Person that has two instance attributes `first_name` and `last_name`. Create a new instance of that
class. Directly accessing the attributes change the value of `first_name` to `David`
and `last_name` to `Alexander`. After that print the new values on the standard output.
"""


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == "__main__":
    person = Person("Petar", "Ivanov")
    person.first_name = "David"
    person.last_name = "Alexander"

    print(f"first_name: {person.first_name} last_name: {person.last_name}")
