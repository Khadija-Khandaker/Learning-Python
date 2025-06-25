# Write a class vector representing a vector of n dimensions. Overloaded the + and * operator which calculates the sum and the dot product of them

class Vector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    
v1 = Vector({1, 2, 3, 4})
print(len(v1))


