from typing import List


class Student:
    # giving a default parameter is not a good idea in this case.  You have 2 students, bob and rolf.
    # when you add a grade for bob, now the list has the grade for bob AND for rolf. change the default to None and
    # grades will be the list of grades if there are any, or an empty list
    # Don't use default values that are mutables
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
