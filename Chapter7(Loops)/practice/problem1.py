# Program to print table of a given number using for loop

num = int (input("Enter a number: "))
i=0

for i in range(0, 11):
    print(f"{num} X {i} = {num * i}")
    