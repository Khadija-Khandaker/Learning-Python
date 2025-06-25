class Employee:
    language = "py" # This is a class attribute
    salary = 50000

harry = Employee()
harry.language = "Javascript" # This is a instance attribute
print(harry.salary, harry.language)


