class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # print out a readable string of the object
        return f"Person {self.name} is {self.age} years old"

    def __repr__(self):  # print out unambigous representation of the object
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)

print(bob)
