# number = 7


# while True:
#   user_input = input("Would you like to play a game? (Y/n) ")

#   if user_input == "n":
#     break

#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#     print("You guessed correctly!")
#     break
#   elif abs(number - user_number) == 1:
#     print("You were off by 1")
#   else:
#     print("Sorry, that's not our number")

# friends = ["Matt", "Blanco", "Terrel", "Markus"]

# for friend in friends:
#     print(f"{friend} is my friend")

# for friend in range(4):
#     print(f"{friends[friend]} is my friend")

grades = [35,67,98,100,100]
total = sum(grades)
amount = len(grades)

print(total/amount)

# for grade in grades:
#   total += grade

# print(total/amount)