class DateOfBirth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"


class Author:
    def __init__(self, f_name: str, l_name: str, dob: DateOfBirth):
        self.first_name = f_name
        self.last_name = l_name
        self.dob = dob

    def __str__(self):
        return f"{self.first_name} {self.last_name} -> {self.dob}"

    @property
    def is_alive(self):
        if 2021 - self.dob.year <= 100:
            return True

        return False


class Book:
    def __init__(self, title: str, author: Author, price: float, pages: int):
        self.id = 0
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.author} - {self.pages} - {self.price}"


class ComicBook(Book):
    def __init__(self, title: str, author: Author, price: float, pages: int, is_colorful: bool):
        super(ComicBook, self).__init__(title, author, price, pages)
        self.is_colorful = is_colorful


class Novel(Book):
    def __init__(self, title: str, author: Author, price: float, pages: int, is_romance: bool):
        super(Novel, self).__init__(title, author, price, pages)
        self.is_romance = is_romance


class Library:
    id_generator = 1

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        book.id = self.id_generator
        self.books.append(book)
        Library.id_generator += 1

    def total_price(self):
        price = 0

        for book in self.books:
            price += book.price

        return price

    def average_pages(self):
        total_pages = 0

        for book in self.books:
            total_pages += book.pages

        if len(self.books) == 0:
            return 0

        return total_pages / len(self.books)


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
