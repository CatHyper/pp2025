from .entity import Entity


class Course(Entity):
    def input(self):
        id =int(input("Enter the course's ID:\n"))
        name = input("Enter the course's name:\n")
        self._id = id
        self._name = name

