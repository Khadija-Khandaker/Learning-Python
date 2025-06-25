class Employee:
    language = "py" # This is a class attribute
    salary = 50000

    def getInfo(self): # It can be write anything instead of self here
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")

    @staticmethod #It is used when we don't want to pass a object 
    def greet():
        print("Good morning")    




harry = Employee() #Employee.getinfo( )
harry.getInfo()
harry.greet()

