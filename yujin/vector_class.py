import math

class Vector:
    # TODO: Finish the Vector class.
    def __init__(self, lst):
        self.vector = list(lst)
    
    def add(self, other):
        v1 = self.vector
        v2 = other.vector
        
        if len(v1) != len(v2):
            print("Cannot add vectors with different lengths")
            return
        
        return Vector([v1[i] + v2[i] for i in range(len(v1))])
        
    def subtract(self, other):
        v1 = self.vector
        v2 = other.vector
        
        if len(v1) != len(v2):
            print("Cannot subtract vectors with different lengths")
            return
        
        return Vector([v1[i] - v2[i] for i in range(len(v1))])

    def dot(self, other):
        v1 = self.vector
        v2 = other.vector

        return sum(v1[i] * v2[i] for i in range(len(v1)))
    
    def norm(self):
        return math.sqrt(sum(item**2 for item in self.vector))

    def __str__(self):
        return '(' + ','.join(str(item) for item in self.vector) + ')'

    def equals(self, other):
        return self.vector == other.vector