# def add(x, y):
#     return x + y


# print(add(5, 7))


# lambda is short function often used without a name, like in use with map.  Not very common

# print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)

doubled = list(map(lambda x: x * 2, sequence))

print(doubled)
