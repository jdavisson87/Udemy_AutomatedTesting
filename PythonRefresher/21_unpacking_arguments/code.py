def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


# print(multiply(1, 2, 3, 4, 5, 6))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 3, 6, 7, operator="*"))


def add(x, y):
    return x + y


nums = [3, 5]
add(*nums)  # destructuring nums

