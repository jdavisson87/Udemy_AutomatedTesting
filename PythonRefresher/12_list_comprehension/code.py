numbers = [1, 3, 5]

# doubled = []
# for num in numbers:
#   doubled.append(num * 2)

doubled = [x * 2 for x in numbers]

# print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Sara", "Jen"]

# starts_s = []
# for friend in friends:
#   if friend.startswith("S"):
#     starts_s.append(friend)

starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)
