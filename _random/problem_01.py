"""
Задача 2. Както всички знаем идва Великден, а покрай Великден зайците имат много работа... Заекът Ставри е 3-кратен сребърен медалист по събиране на яйца и тази година е решен да спечели златото. От вас той иска да му направите кошница за състезанието (само с най-добрата кошница може горкият Ставри да се надява да триумфира).
По регламент всяко яйце се описва от уникален низ с точна дължина и неговата големина. Тъй като е състезание и всичко си има правила, той не може да използва каква да е кошница... Всяка кошница си има име и то е името на нейният собственик. Кошницата, която ще му направите трябва да може да променя размера си според това колко яйца има в нея - а това както сами предполагате е доста трудно. За това във всеки един момент, ако в нея има N яйца, то тя може да има свободно място за най-много още N яйца. Кошницата, която ще му осигурите трябва да позволява добавянето на ново яйце и премахването на яйце по даден низ, който го описва.
Всяка вечер кошниците на участниците трябва да се виртуализират някъде, затова от вашата програма, Ставри иска да може да сериализира кошницата си в бинарен формат (масив), като заеманото място е минимално, тоест низовете заемат точно толкова, колкото са дълги или константно число байтове повече. А на сутринта прогамата ви ще трябва да десериализира кошницата от бинарния формат.
В края на състезанието съдиите трябва да могат да преценят кой печели, затова трябва да предоставите функция която по зададена кошница генерира репорт за нейното съдържание. Ще трябва да го запишете в текстов файл с име : "report_nameOfBasket.txt", където nameOfBasket е името на кошницата за която генерирате репорт в момента. Вътре трябва да са описани всички яйца (чрез уникалния низ и тяхната големина). Всяко яйце трябва да се намира на нов ред.

Задача 3. С вашите кошници по вашата глава...
Добре познатият ви Ставри спечели това пусто злато. Той искрено ви благодари. Но... сега реши да отвори бизнес, защото чул, че от математиката се правели добри пари. Ще продава математически кошници, представете си... И разбира се пак вие трябва да спасявате положението - Той ви моли да добавите следните оператори към кошницата, която му направихте:
Оператор [] - който по зададен индекс, ако той е валиден, връща яйцето, което се намира там.
Оператор [] - който по зададен символен низ, връща първото яйце, което го съдържа, ако има такова.
Оператори +, += - които конкатенират 2 кошници (работят върху аргументи две кошници).
Оператори +, += - които конкатенират низ с всички яйца в дадена кошницата. (два аргумента - кошница и низ)
Оператори *, *=  - приемат цяло число и умножават всички размери на яйца в кошницата по това число. (аргументи кошница и число)
Оператори /, /= - приемат цяло число и делят всички размери на яйца в кошницата на даденото число. (аргументи кошница и число)
Оператори %, %= - които пресмятат сечението на кошници (работят върху аргументи две кошници).
Оператори (==, !=, <, <=, >=) - сравнява две кошници, като две кошници са равни, когато всеки елемент на позиция i в първата кошница е равен на елемента на същата позиция във втората. А първата кошница е по-малка от втората, когато срещнете елемент в първата, който е по-малък от съответния във втората и до момента не сте срещнали по-голям елемент в първата. Две яйца са равни едно на друго ако низовете в тях са еднакви, а едно яйце е по-малко от друго яйце, ако низа на първото яйце е по-малък в лексикографски смисъл от низа във второто.
За яйцата трябва да дефинирате поне 10 оператора, по ваш избор. Подберете ги така, че да улеснят максимално реализацията на кошница.
Напишете и програма с която да покажете използването на операторите.
Понеже Ставри вече е спечелил кошницата, която му написахте сега се изисква да я надградите (без да губите функционалност). Т.е. имплементацията на домашно 3 не трябва да премахва нищо, което е работело в домашно 2. Можете да преправята или дори да пренаписвате вашето домашно 2, ако надграждането не е възможно. И не забравяйте да съблюдавате добрите практики при писането на кода - все пак ще се продава ;)
"""

import copy


class Egg:
    def __init__(self, egg_id: str, size: float):
        self.id = egg_id
        self.size = size

    def __str__(self):
        return f"{self.id} - {self.size}"

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id


class Basket:
    def __init__(self, owner_name: str):
        self.name = owner_name
        self.eggs = []

    def add_egg(self, egg: Egg):
        if self.__get_egg_index_by_id(egg.id) == -1:
            # We'll add the egg only if it's not already part of the basket
            self.eggs.append(egg)

    def __get_egg_index_by_id(self, egg_id: str) -> int:
        for index in range(len(self.eggs)):
            if self.eggs[index].id == egg_id:
                return index

        # If the egg was not found the function will return -1 (don't mistake it for negative index)
        return -1

    def remove_egg(self, egg_id: str):
        egg_index = self.__get_egg_index_by_id(egg_id)

        if egg_index != -1:
            # Only if the egg was found we want to remove it from the list
            self.eggs.pop(egg_index)

    def create_report(self):
        with open(f"report_{self.name}", "w") as fd:
            for egg in self.eggs:
                fd.write(str(egg))
                fd.write("\n")  # Writes a special character for new line after each egg in the basket

    def __getitem__(self, item: int):
        if isinstance(item, int) and 0 <= item < len(self.eggs):
            # if the item is valid and is of type int
            return self.eggs[item]
        if isinstance(item, str):
            # if the item is of type string
            index = self.__get_egg_index_by_id(item)
            if index != -1:
                # if there is an egg with such id
                return self.eggs[index]

    def __add__(self, other):
        basket = Basket(self.name + " " + other.name)

        for egg in copy.deepcopy(self.eggs):
            basket.add_egg(egg)

        for egg in copy.deepcopy(other.eggs):
            basket.add_egg(egg)

        return basket

    def __iadd__(self, other):
        self.name += " " + other.name

        for egg in copy.deepcopy(other.eggs):
            self.eggs.append(egg)

    def __mul__(self, power):
        basket = Basket(self.name)

        for egg in copy.deepcopy(self.eggs):
            basket.add_egg(egg)

        for egg in basket.eggs:
            egg.size *= power

        return basket

    def __imul__(self, power):
        for egg in self.eggs:
            egg.size *= power

    def __truediv__(self, div):
        basket = Basket(self.name)

        for egg in self.eggs:
            basket.add_egg(egg)

        for egg in basket.eggs:
            egg.size /= div

        return basket

    def __idiv__(self, div):
        for egg in self.eggs:
            egg.size /= div

    # IMPORTANT! - the following operators work because you can compare lists and since we have implemented
    # comparison for Egg we can compare lists of eggs
    def __eq__(self, other):
        return self.eggs == other.eggs

    def __ne__(self, other):
        return self.eggs != other.eggs

    def __lt__(self, other):
        return self.eggs < other.eggs

    def __le__(self, other):
        return self.eggs <= other.eggs

    def __gt__(self, other):
        return self.eggs > other.eggs

    def __ge__(self, other):
        return self.eggs >= other.eggs

    def __mod__(self, other):
        conjunction_basket = Basket("Conjunction")

        for egg in copy.deepcopy(self.eggs):
            for other_egg in other.eggs:
                if egg == other_egg:
                    # We can compare directly because we have implemented the __eq__ magic method for EGG
                    conjunction_basket.add_egg(egg)

        return conjunction_basket

    def __str__(self):
        return f"===== {self.name} =====\n" + "\n".join([str(egg) for egg in self.eggs])


if __name__ == '__main__':
    basket_a = Basket("Basket A")
    basket_a.add_egg(Egg("000", 3.14))
    basket_a.add_egg(Egg("001", 3.17))
    basket_a.add_egg(Egg("002", 4.0))
    print(basket_a)

    basket_b = Basket("Basket B")
    basket_b.add_egg(Egg("001", 3.0))
    basket_b.add_egg(Egg("002", 7.1))
    basket_b.add_egg(Egg("003", 1.1))
    basket_b.add_egg(Egg("004", 4.4))
    print(basket_b)

    # the plus operator
    print(basket_a + basket_b)
    # the mul operator
    print(basket_a * 2)
    # the div operator
    print(basket_a / 2)
    # the mod operator
    print(basket_a % basket_b)
    # The comparison operators
    print("==", basket_a == basket_b)
    print("!=", basket_a != basket_b)
    print("<", basket_a < basket_b)
    print("<=", basket_a <= basket_b)
    print(">", basket_a > basket_b)
    print(">=", basket_a >= basket_b)
