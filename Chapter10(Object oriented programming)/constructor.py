class Employee:
    language = "py" # This is a class attribute
    salary = 50000

    def __init__(self, name, salary, language): # dunder method which is called automatically(starts with double underscore)
         self.name = name
         self.salary = salary
         self.language = language
         print("I am creating an object")

    def getInfo(self): # It can be write anything instead of self here
        print(f"The language is {self.language}. The salary is {self.salary}")

    

    @staticmethod #It is used when we don't want to pass a object 
    def greet():
        print("Good morning")    




harry = Employee("Harry",13000, "Javascript") #Employee.getinfo( )
print(harry.name, harry.salary, harry.language)

rohan = Employee("Rohan", 15000, "C++")
print(rohan.name, rohan.salary, rohan.language)

