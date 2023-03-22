class Book:
    def __init__(self, id, title, author, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == "available":
            self.borrowed_books.append(book)
            book.status = "borrowed"
        else:
            print(f"{book.title} is not available.")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.id] = book

    def remove_book(self, id):
        if id in self.books:
            del self.books[id]
        else:
            print(f"Book with ID: {id} not found.")

    def add_member(self, member):
        self.members[member.id] = member

    def find_book(self, id):
        return self.books.get(id)

    def find_member(self, id):
        return self.members.get(id)

    def display_books(self):
        for book in self.books.values():
            print(book)
