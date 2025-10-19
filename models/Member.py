from abc import ABC, abstractmethod

class Member(ABC):
    def display_role(self):

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
    @abstractmethod
    def display_role(self):
        pass
        # this is a placeholder
        # it does not contribute anything to the function



    def normal_function(self):
        pass
