class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print(f"Added '{title}' to library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed '{title}'.")
                return
        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print(f"Issued '{title}'.")
                return
        print("Book unavailable or not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print(f"Returned '{title}'.")
                return
        print("Book cannot be returned.")


lib = Library()
lib.add_book("Mathematics")
lib.issue_book("Mathematics")
lib.return_book("Mathematics")
lib.remove_book("Mathematics")