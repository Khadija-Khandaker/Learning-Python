# Write a list comprehension to print a list which Contains the multipluation table of a user entered number.

n = int (input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)