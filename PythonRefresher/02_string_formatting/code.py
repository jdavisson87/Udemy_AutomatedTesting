name = "Jeff"

# print(f"Hello {name}")

# name = "Bob"

# print(f"Hello {name}")

greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Bob")

print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}.  Today is {}"
formatted = longer_phrase.format(name, "Wednesday")

print(formatted)