e = set() #Empty set. s={} means empty dictionary
print(type(e))

s = {1, 5, 7, 32, 5, 5, "Hello"}

# Methods
s.add(24)
print(s, type(s))

s.remove(5)
print(s, type(s))

# Union & Intersection
s1 = {1, 5, 8, 14, 9}
s2 = {2, 5, 10, 14, 7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)

print({9,5}.issubset(s1))

s.clear()
print(s)


