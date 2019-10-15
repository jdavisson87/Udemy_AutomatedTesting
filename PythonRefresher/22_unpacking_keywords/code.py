def named(name, age):  # ** collects keyword arguments
    print(name, age)


# named(name="Bob", age=25)

details = {"name": "Bob", "age": 25}

named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(**details)
