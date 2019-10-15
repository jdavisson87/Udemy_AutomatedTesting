# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student["grades"]))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


rolf = Student("Rolf", (100, 100, 93, 78, 90))
bob = Student("Bob", (90, 90, 93, 78, 90))

print(rolf.name)
print(rolf.average_grade())
print(bob.name)
print(bob.average_grade())
