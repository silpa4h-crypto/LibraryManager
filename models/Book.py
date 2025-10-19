class Book:
    # Constructor
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.isbn = isbn
        self.is_issued = False

    # Getters and setters methods
    # Encapsulation

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.isbn

    def get_is_issued(self):
        return self.is_issued

    def issue(self):
        self.is_issued = True

    def issue_book(self):
        self.is_issued = True


class Student:
    pass