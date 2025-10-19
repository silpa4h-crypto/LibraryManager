class Library:

    # Attributes: name, collection of books

    # Functionalities:
    # add new books
    # display the books
    # issue books
    # return the book

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_book(self):
        print(f"Books {self.name}")
        print("*******")

        for book in self.books:
            print(f"{book}")

    def issue_book(self, book):
        if book in self.books and not book.is_issued():
            book.issue()
            return True #confirmation for issuing the book
        return False    #failed to issue the book




    def return_book(self, book):
        if book in self.books and book.is_issued():
            print(f"returning the book was successful")
            return True
            print(f"returning the book was not successful")
