# Recap of strings are immutable
a = "hello"
print(a[0])
print(a[2])
# a[3]="i" # It is not possible because strings are immutable

#List
list = ["apple","orange","Rohan",5.98,33,False] # can store different data types in list

print(list)
print(list[5])

list[4]=56   # Unlike strings list are mutable
print(list[4])

list[2]="Akash"  # Unlike strings list are mutable
print(list[2])

# slicing of list
print(list[1:5])

# Methods of list
# Appendic method
list.append("hello")
list.append(55)
print(list)

# Sort method
l1 = [99,8,44.67,44.66,23]
l1.sort()
print(l1)

# Reverse method
l1.reverse()
print(l1)

# Insert method
l1.insert(3,0) # Insert 0 such that its index number in the list is 3 
print(l1)

# Pop method
print(l1.pop(3))
print(l1)

# Remove method 
l1.remove(23)
print(l1)

