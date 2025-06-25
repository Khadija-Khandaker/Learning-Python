class Employee:
    language = "py" # This is a class attribute
    salary = 50000

harry = Employee()
harry.name = "Harry" # This is a instance attribute
print(harry.name, harry.salary, harry.language)

Rohan = Employee()
Rohan.name = "Rohan"
print(Rohan.name, Rohan.salary, Rohan.language)
