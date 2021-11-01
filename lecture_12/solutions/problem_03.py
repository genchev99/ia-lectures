"""
Reuse the class definition from `Problem 02`.

- make `grades` a private property
- make `first_name` and `last_name` protected

- Create a new private method `__average()` that calculates the average grade of the student.
- Create a new public method `add_grade(grade: float)` that adds a new grade to the student grades (make sure that the
  grade is valid).
- Create a new public method `get_score() -> str:` that returns information for the student in the following format
  `"{id}, {first_name} {last_name}, {average_grade}"`

Make a couple of students and store them in a list. Add various grades to them and for each of them print their `score`.
"""


class Student:
    id_auto_increment = 1

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
        self.id = self.id_auto_increment
        self.__grades = []

        # Don't forget to auto increment the class attribute
        Student.id_auto_increment += 1

    def __average(self) -> float:
        if len(self.__grades) == 0:
            return 0.0

        return sum(self.__grades) / len(self.__grades)

    def add_grade(self, grade: float):
        if grade < 2.0 or grade > 6.0:
            raise ValueError("Invalid grade!")

        self.__grades.append(grade)

    def get_score(self) -> str:
        return f"{self.id}, {self._first_name} {self._last_name}, {self.__average()}"


if __name__ == "__main__":
    students = [
        Student("Ivan", "Ivanov"),
        Student("Petar", "Petrov"),
        Student("Dimitar", "Dimitrov"),
    ]

    # Add grades to the first student
    students[0].add_grade(5.6)
    students[0].add_grade(3.1)
    students[0].add_grade(2.6)

    # Add grades to the second student
    students[1].add_grade(4.6)
    students[1].add_grade(4.1)
    students[1].add_grade(5.1)
    students[1].add_grade(6.0)

    for student in students:
        print(student.get_score())
