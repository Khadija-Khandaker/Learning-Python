# 1) Program to store 7 fruits in a list entered ny the user
fruits = []

f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)

print(fruits)

# 2) Program to accept marks of 6 students and display them in a sorted manner
marks = []

m1 = int(input("Enter your mark: "))
marks.append(m1)
m2 = int(input("Enter your mark: "))
marks.append(m2)
m3 = int(input("Enter your mark: "))
marks.append(m3)
m4 = int(input("Enter your mark: "))
marks.append(m4)
m5 = int(input("Enter your mark: "))
marks.append(m5)
m6 = int(input("Enter your mark: "))
marks.append(m6)
marks.sort()

print(marks)


# 4) Program to sum a list with 4 number
l = [1,2,3,4]
print(sum(l))

# 5) Program to count the number of zeros in the following tuple - a=(7,0,8,0,0,9)
a = (7,0,8,0,0,9)
print(a.count(0))

# 3) Check that tuple type can not be changed in python
a = (1,4,"hello",False)
a[0] = 2 # Can't change