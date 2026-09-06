#Tuple

# Tuple — The Immutable List
# A tuple is exactly like a list, except you cannot change it once created.
# Use tuples for data that should stay constant — like days of the week, coordinates, or config values.

#days = ("Mon", "Tue", "Wed")

#print(days[0])   # Mon
#days[0] = "X"   # ❌ TypeError — tuples are immutable
# Tuple Methods (Only 2!)
#t = (1, 2, 3, 2, 1)
#t.index(2)    # → 1  (first position of 2)
#t.count(2)    # → 2  (2 appears twice)

w = ["Monday", "Tuesday", "Wednesday", "Thusday", "Friday", "Saturday", "Sunday"]

week = tuple(w)
print(week)
print(type(week))

print(week(-1))
