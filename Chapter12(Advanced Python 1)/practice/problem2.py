#  Write a program to print third, fifth and seventh element from a list using enumerate function

l = [1, 8, 6, 2, 45, 23, 35, 78]

for i, item in enumerate(l):
    if (i == 2 or i ==4 or i == 6):
        print(item)