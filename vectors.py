class Vec:
    def __init__(self, contents = []):
        """constructor defaults to empty vector
           accepts list of elements to initialize a vector object with the 
           given list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """Overloads the built-in function abs(v)
            returns the Euclidean norm of vector v
        """
        square = 0
        v = []
        w = [v.append(self.elements[i]**2) for i in range(len(self.elements))]
        i = 0
        while(i!= len(v)):
            square = square + v[i]
            i = i + 1
        norm = math.sqrt(square)
        return norm
        
    def __add__(self, other):
        """Overloads the + operation to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) == len(other.elements):
            v = []
            w = [v.append(self.elements[i] + other.elements[i]) for i in range(len(self.elements))]
            return v
        else: 
            raise ValueError
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            #FIXME: IMPLEMENT
            if len(self.elements) == len(other.elements):
                product = 0
                v = []
                w = [v.append(self.elements[i] * other.elements[i]) for i in range(len(self.elements))]
                i = 0
                while( i != len(v)):
                    product +=v[i]
                    i = i + 1
                return product
            else:
                raise ValueError
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            v = []
            w = [v.append(self.elements[i] * other) for i in range(len(self.elements))]
            return Vec(v)
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        if type(other) == float or type(other) == int:
            v = []
            w = [v.append(self.elements[i] * other) for i in range(len(self.elements))]
            return Vec(v)
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation
    
    def __sub__(self, other):
        if len(self.elements) == len(other.elements):
            v = []
            w = [v.append(self.elements[i] - other.elements[i]) for i in range(len(self.elements))]
            return Vec(v)

import math
u = Vec([1, 2, 3])
w = Vec([0, 1, -1])
v = Vec([0, -3])
print("u = ", u)
print("w = ", w)
print("Euclidean norm of u:", abs(u))
print("Expected:", math.sqrt(sum([ui**2 for ui in u.elements])))
print("Euclidean norm of u:", abs(v))
print("Expected: 3")
print("\nu left scalar multiplication by 2:", 2*u)
print("Expected: [2, 4, 6]")
print("\nw right scalar multiplication by -1:", w * -1.2)
print("Expected: [0, -1, 1]")
print("\nVector addition:", u + w)
print("Expected: [1, 3, 2]")
print("\nVector addition:", u - w)
print("Expected: [1, 1, 4]")
print("\nDot product:", w*u)
print("Expected: -1")


try:
    print("\nDot product:", v*u)
    print("If this line prints, you forgot to raise a ValueError for taking the dot product of vectors of different lengths")
except:
    print("If this line prints, the line passed the test.")
