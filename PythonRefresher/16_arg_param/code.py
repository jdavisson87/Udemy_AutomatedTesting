# y is a default parameter.  x is a required parameter.  if you run the function, you must
#  give a value for x and if you don't give a value for y, it will default to 8
# if you made x a default parameter, then y must also have a default parameter


def add(x, y=8):
    print(x + y)


add(2, 3)


def say_hello(name):
    return f"Hello {name}"


name = input("What is your name? ")

print(say_hello(name))
