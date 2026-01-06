class Entity:
    def __init__(self):
        self._id = 0
        self._name = ''
    
    def input(self):
        id =input("Enter the ID:\n")
        name = input("Enter the name:\n")
        self._id = id
        self._name = name
    def list(self):
        print(f"{self._id} | {self._name}")
    
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def __str__(self):
        return f"{self._id},{self._name}"
