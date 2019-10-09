friends = {"Matt", "Markus", "Sarah"}
abroad = {"Matt", "Sarah"}

local_friends = friends.difference(
    abroad
)  # calls difference function and remove elements that are in both sets

print(local_friends)

local = {"Jeff", "Terrel"}
away = {"Blanco", "Nick"}

new_friends = local.union(away)

print(new_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
