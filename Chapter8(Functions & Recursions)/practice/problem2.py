# Write a python program using function to convert Celsius to Fahrenheit

def temperature(c):

    f = ((9*c)/5) + 32
    print(f"{round(f,2)}° F")

c = int(input("Enter temperature in celsius: "))
temperature(c)    