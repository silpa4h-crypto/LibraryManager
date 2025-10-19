from models.Member import Member


class Student(Member):

   def __init__(self, name, user_id):
       Member.__init__(self, name, user_id)


   def display_role(self):
       print('This refers to a student')


   def dummyFunction(self):
       print("there's nothing here")
