# Write a python function which converts inches to cms
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter a value in inches: "))

print(f"cms = {inch_to_cms(n)}")


