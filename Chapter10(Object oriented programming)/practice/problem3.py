# Create a class with a class attribute a: create an object from it and set "a" directly using object.a=0. Does this change the class attribute

class Demo:
    a = 4


o = Demo()
print(o.a)  # prints the class attribute because there is no instance attribute
o.a = 0       # instance attribute is set
print(o.a)       # prints the instance attribute because instance attribute is present
print(Demo.a)       # print the class attribute 