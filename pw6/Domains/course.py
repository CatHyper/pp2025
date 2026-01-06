from .entity import Entity


class Course(Entity):
    def __init__(self):
        super().__init__()
        self._credits = 0

    def input(self):
        id = int(input("Enter the course's ID:\n"))
        name = input("Enter the course's name:\n")
        credits = int(input("Enter the course's credits:\n"))
        self._id = id
        self._name = name
        self._credits = credits

    def get_credits(self):
        return self._credits

    def __str__(self):
        return f"{self._id},{self._name},{self._credits}"

