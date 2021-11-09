class Soldier:
    def __init__(self, name: str, age: int, fighting_level: int, salary: int):
        self.name = name
        self.age = age
        self.fighting_level = fighting_level
        self.salary = salary


class Sergeant(Soldier):
    def __init__(self, name: str, age: int, fighting_level: int, salary: int, squad_description: str, soldiers: list):
        super(Sergeant, self).__init__(name, age, fighting_level, salary)

        self.squad_description = squad_description
        self.soldiers = soldiers


class Spell:
    def __init__(self, description: str, spell_type: str, required_magic_power: int):
        self.description = description
        self.spell_type = spell_type
        self.required_magic_power = required_magic_power


class MagicBook:
    def __init__(self):
        self.spells = []


class Wizard(Soldier):
    def __init__(self, name: str, age: int, fighting_level: int, salary: int, battalion_description: str,
                 sergeants: list, magic_power: int, magic_book: MagicBook):
        super(Wizard, self).__init__(name, age, fighting_level, salary)

        self.battalion_description = battalion_description
        self.sergeants = sergeants
        self.magic_power = magic_power
        self.magic_book = magic_book


class Commander(Soldier):
    def __init__(self, name: str, age: int, fighting_level: int, salary: int, army_description: str, wizards: list):
        super(Commander, self).__init__(name, age, fighting_level, salary)

        self.army_description = army_description
        self.wizards = wizards

    def army_battle_level(self):
        fighting_level = 0
        fighting_level += self.fighting_level

        for wizard in self.wizards:
            fighting_level += wizard.fighting_level

            for sergeant in wizard.sergeants:
                fighting_level += sergeant.fighting_level

                for soldier in sergeant.soldiers:
                    fighting_level += soldier.fighting_level

        return fighting_level

    def army_magic_level(self):
        pass

    def army_cost(self) -> int:
        pass


if __name__ == '__main__':
    soldiers = [
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
        Soldier("pesho", 10, 1, 5),
    ]

    sergeant = Sergeant("pesho", 10, 1, 5, "pesovci", soldiers)
    wizard = Wizard("pesho", 10, 1, 5, "pesovci", [sergeant], 10, MagicBook())
    commander = Commander("pesho", 10, 1, 5, "peshovci", wizards=[wizard])

    print(commander.army_battle_level())
