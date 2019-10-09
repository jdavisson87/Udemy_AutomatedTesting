movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"You have watched {user_movie} before.  Must be good")
else:
    print("You haven't watched that yet.")

