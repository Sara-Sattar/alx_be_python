class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} - {self.page_count} pages"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} - {self.file_size}MB"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        for book in self.books:
            print(book)


if __name__ == "__main__":
    # Exemple d'utilisation
    lib = Library()
    b1 = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)
    b2 = EBook("Python 101", "Michael Driscoll", 5)

    lib.add_book(b1)
    lib.add_book(b2)

    lib.list_books()
