from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def add_grade(self, subject, grade):
        pass

    @abstractmethod
    def average_grade(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class DetailsMixin:
    def display_details(self):
        return f"ID: {self._student_id}, Student: {self.name}, Average Grade: {self.average_grade()}"


class Student(DetailsMixin, Person):
    def __init__(self, student_id, name):
        self._student_id = student_id
        self.name = name
        self.grades = {}

    @property
    def student_id(self):
        return self._student_id

    def add_grade(self, subject, grade):
        if grade >= 0:
            self.grades[subject] = grade
        else:
            print("Please, insert a non-negative number")

    def average_grade(self):
        total_grade = 0
        for grade in self.grades:
            total_grade += self.grades.get(grade)
        avg_grade = total_grade/len(self.grades)
        return avg_grade


class StudentManagementSystem(DetailsMixin):
    def __init__(self):
        self.student = Student
        self.student_base = {}

    def add_student(self, id_number, name):
        self.student_base[id_number] = name

    def show_student_details(self):
        if self.student.student_id in self.student_base.keys():
            show = super().display_details()
            return show
        else:
            return "The named student doesn't exist"

    def show_student_average_grade(self):
        return self.student.average_grade

