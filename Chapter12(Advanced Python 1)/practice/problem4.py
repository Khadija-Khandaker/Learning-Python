# Write a program to display a/b where a and b are integers. If b=0, display Infinite by handling the Zero Division Error.


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))

    print(a/b) 



except ZeroDivisionError as v:
    print("Infinite")