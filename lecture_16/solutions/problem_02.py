class Employee:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.id = ""
        self.department = ""
        self.salary = 0.0


class Specialist(Employee):
    def __init__(self):
        super(Specialist, self).__init__()
        self.description = ""


class ChiefOfDepartment(Specialist):
    def __init__(self):
        super(ChiefOfDepartment, self).__init__()
        self.department_description = ""
        self.employees = []


class Secretary:
    def __init__(self):
        self.languages = []


class Director:
    def __init__(self):
        self.secretary = Secretary()
        self.employees = []


if __name__ == '__main__':
    director = Director()
