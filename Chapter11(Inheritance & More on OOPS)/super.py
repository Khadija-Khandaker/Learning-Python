class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
        def __init__(self):
                print("Constructor of programmer")
        b =2

class Manager(Programmer):
        def __init__(self):
                super().__init__()
                print("Constructor of manager")
        c = 3

o = Employee()
print(o.a)     # prints the a attribute   
#print(o.b)      # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)