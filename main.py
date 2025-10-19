from models.Book import Book
from models.Member import Member
from models.student import Student
from models.librarian import Librarian
if __name__ == '__main__':
    harryPotter =Book("harry Potter", "j.k rawling", 'fantacy001')
    print(harryPotter.isbn)
    print(harryPotter.is_issued)
    print(harryPotter.get_title())


    # member1 = Member(name:"mohanlal", user_id:"2255")
    # print(member1.name)

    student1 = Student(name: 'Indhu' , user_id:"2255")
    print(student1.name)
    student1.display_role()


   # student1.dummyFunction()

    librarian = librarian(name:"malu" ,userid:'malu0025')
    print(librarian.name)
    librarian.display_role()


