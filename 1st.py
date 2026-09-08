class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")

    def return_book(self):
        self.is_borrowed = False
        print("Book returned successfully")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully")

    def borrow_book(self, book, patron):
        if book.is_borrowed == False:
            book.borrow()
            patron.borrowed_books.append(book.title)
        else:
            print("Book is not available")

    def return_book(self, book, patron):
        book.return_book()
        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)


# Main Program

library = Library()

book1 = Book("Python Basics", "Varad", 101)
library.add_book(book1)

patron1 = Patron("Rahul", 1)
library.register_patron(patron1)

library.borrow_book(book1, patron1)

print(patron1.borrowed_books)

library.return_book(book1, patron1)

print(patron1.borrowed_books)