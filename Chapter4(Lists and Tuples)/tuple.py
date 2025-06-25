# Making tuple
a = (1,)  # One element tuple 
print(type(a)) 

a = (1,3,5,3,7,False,"Akash")
print(a)

# t[2] = 22 # Can't be change because tuple is immutable

# Methods of tuple
t = a.count(3) # Count method
print(t) 

i = a.index("Akash") # Index method
print(i)

print(4 in a)
print(False in a)

print(len(a))

print(a[1:4]) #Slicing



 
