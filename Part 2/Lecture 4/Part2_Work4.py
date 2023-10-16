class Student:
    university = "Skillwill"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, grade: {self.grade}"

    @property
    def is_passing(self):
        if self.grade > 60:
            return True
        return False

    def increase_grade(self, value):
        self.grade += value
