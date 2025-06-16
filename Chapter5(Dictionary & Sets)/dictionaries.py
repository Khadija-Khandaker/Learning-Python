m={} #Empty dictionary

marks = {
    "A": 100,
    "B": 70,
    "C": 90, 
     5:"E" 
}

print(marks, type(marks))
print(marks["C"])

# Methods
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"A":99,"D":87} )
print(marks)

print(marks.get("A"))
print(marks.get("F")) # Prints none
# print(marks["F"]) # Returns an error

marks.pop("A")
print(marks)

print(marks.popitem()) # Remove the last item from the dictionary
print(marks)







