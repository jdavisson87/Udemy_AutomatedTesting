# t = 5, 11
# x, y = t
# print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

person = ("Bob", 42, "Mechanic")
name, _, profession = person #underscore variable means it is to never be used, it is a blank variable

#head, *tail = [1,2,3,4,5] #first value is head, rest of the values will be stored in tail
*head, tail = [1,2,3,4,5] #tail gets the last value, head gets the rest