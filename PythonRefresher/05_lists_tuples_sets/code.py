l = ["Jeff", "Matt", "Markus"]  # can add and remove elements from a list, keeps order
t = ("Jeff", "Matt", "Markus")  # can't modify tuple
s = {
    "Jeff",
    "Matt",
    "Markus",
}  # you can add and remove elements, but you can't have duplicates.  Order is not guaranteed

print(l[2])
print(t[0])

l[0] = "Kittaka"
l.append("Smith")
print(l)

l.remove("Matt")

print(l)

s.add("Smith")
print(s)
