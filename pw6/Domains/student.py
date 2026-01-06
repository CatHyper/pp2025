from .entity import Entity

class Student(Entity):
    def __init__(self):
        super().__init__()

        self.__dob = ''
        self.gpa = 0.0
    def input(self):
        id =int(input("Enter the student's ID:\n"))
        name = input("Enter the student's name:\n")
        dob = input("Enter the student's DoB:\n")
        self._id = id
        self._name = name
        self.__dob = dob
    def list(self):
        print(f'ID: {self._id} | Name: {self._name} | DoB: {self.__dob}')

    def get_gpa(self):
        return self.gpa

    def __str__(self):
        return f"{self._id},{self._name},{self.__dob}"
