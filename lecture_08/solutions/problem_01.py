class Student:
    def __init__(self, student_id: int, student_name: str):
        self.id = student_id
        self.name = student_name

    def display(self) -> None:
        print(self.id, self.name)


student = Student(42, "pesho")
student.display()
