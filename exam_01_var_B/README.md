# Задача 1

Даден а лист със цели положителни числа `x`. Казваме, че едно число е специално ако:

- то се дели на `2`
- не е между `7` и `21` (включително)
- сумата от числата му не се дели на `3`
- втората цифра на числото (ако има такава) е различна от `3`

Да се напише функцията `sum_of_special_numbers(x: list) -> int`, която да сумира всички специални числа в даден лист и
да връща резултата.

### Пример

```
[35, 31, 19, 61, 8, 77, 11, 10, 17, 25, 73, 47, 76, 50, 28, 98, 7, 61, 56, 85] -> [76, 50, 28, 98, 56] -> 308
[27, 30, 75, 18, 59, 81, 12, 35, 96, 99, 61, 10, 56, 70, 86, 10, 51, 38, 45, 5] -> [56, 70, 86, 38] -> 250
[2, 98, 44, 13, 75, 59, 19, 45, 54, 93, 81, 58, 38, 31, 96, 3, 36, 0, 64, 5] -> [2, 98, 44, 58, 38, 64] -> 304
[51, 10, 97, 39, 54, 54, 98, 47, 71, 55, 64, 4, 0, 10, 52, 51, 97, 94, 80, 59] -> [98, 64, 4, 52, 94, 80] -> 392
[63, 94, 57, 22, 24, 95, 20, 30, 46, 30, 49, 43, 85, 42, 47, 55, 52, 63, 1, 7] -> [94, 22, 46, 52] -> 214
```

# Задача 2

1. Да се имплементира клас `Author` (Автор на книга), който да има следните атрибути

- `first_name` - собственото име на автора
- `last_name` - фамилията на автора
- `birth_year` - рожденната година на автора

> Имплементирайте конструктор, с който да могат да се задават стойности на тези полета. Използвайте подходящи типове данни

2. Да се имплементира клас `Book` (Книга), който да има следните атрибути:

- `title` - Заглавието на книгата
- `author` - Авторът на книгата `(1)`
- `price` - Цената на книгата
- `pages` - Размерът на книгата в страници

> Имплементирайте конструктор, с който да могат да се задават стойности на тези полета. Използвайте подходящи типове данни

3. Да се имплементира клас `ComicBook` (Комикс), който наследява `Book` и има следните нови атрибути:

- `is_colorful` - булева променлива, която е истина, ако комиксът е цветен и лъжа в противен случай

> Имплементирайте конструктор, с който да могат да се задават стойности на тези полета. Използвайте подходящи типове данни

4. Да се имплементира клас `Novel` (Новела), който наследява `Book` и има следните нови атрибути:

- `is_romance` - булева променлива, която е истина, ако новелата е "romance" и лъжа в противен случай

> Имплементирайте конструктор, с който да могат да се задават стойности на тези полета. Използвайте подходящи типове данни

5. Да се имплементира клас `Library` (Библиотека), който да има следните атрибути и методи:

- `books` - `(2, 3, 4)` списък с книгите, които са част от библиотеката
-
- `add_book(book)` - метод на класа, чрез който се добавят нови книги
- `total_price()` - метод на класа, който връщата цената на всички книги в библиотеката
- `average_pages()` - метод на класа, който връща средната стойност на броя на страниците на книгите в библиотеката

> Имплементирайте конструктор, с който да могат да се задават стойности на тези полета. Използвайте подходящи типове данни

### Примерно използване и изход

```python
if __name__ == '__main__':
    library = Library()

    stan_lee = Author("Stan", "Lee", DateOfBirth(1922, 12, 28))
    library.add_book(ComicBook("Spider man", stan_lee, 19.99, 30, True))
    library.add_book(ComicBook("Iron man", stan_lee, 15.50, 20, True))
    library.add_book(ComicBook("Batman", stan_lee, 9.99, 13, False))

    ernest_hemingway = Author("Ernest", "Hemingway", DateOfBirth(1899, 7, 21))
    library.add_book(ComicBook("The old man and the sea", ernest_hemingway, 29.99, 345, False))
    library.add_book(ComicBook("The Torrents of Spring", ernest_hemingway, 18.20, 279, False))
    library.add_book(ComicBook("The Sun Also Rises", ernest_hemingway, 16.20, 160, True))
    library.add_book(ComicBook("Winner Take Nothing", ernest_hemingway, 40.00, 450, True))

    print("total price: ", library.total_price())  # total price:  149.87
    print("average pages: ", library.average_pages())  # average pages:  185.28571428571428
```

### Бонуси

- Имплементирайте подходящи `magic методи` за визуализиране на класовете - `__str__`.
- Добавете ауто-генерирано `ID` към всяка новодобавена книга
- Добавете property `is_alive` (използвайте декоратора @property) към `Author`, който да връща `True`, ако авторът е на
  по-малко от 100 години и `False` в противен случай.
