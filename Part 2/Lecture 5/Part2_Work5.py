class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Mixin:
    def return_dict(self):
        return self.__dict__


class Student(Mixin, Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university
