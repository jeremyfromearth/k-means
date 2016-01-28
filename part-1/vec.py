from math import sqrt

class Vec(): 

    @staticmethod
    def distance(v1, v2):
        delta = v1 - v2
        return sqrt(delta.x ** 2.0 + delta.y ** 2.0)

    @staticmethod
    def zero():
        return Vec(0.0, 0.0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)
    
    def dot(self, v):
        return self.x * v.x + self.y * v.y

    def normalized(self):
        return self / self.length

    def __eq__(a, b):
        return a.x == b.x and a.y == b.y

    def __add__(a, b): 
        return Vec(a.x + b.x, a.y + b.y)

    def __iadd__(a, b):
        a.x += b.x
        a.y += b.y
        return a

    def __sub__(a, b):
        return Vec(a.x - b.x, a.y - b.y)

    def __isub__(a, b):
        a.x -= b.x
        a.y -= b.y
        return a

    def __mul__(a, b):
        if isinstance(a, (float, int, complex)):
            return Vec(a.x * b, a.y * b) 
        return Vec(a.x * b.x, a.y * b.y)

    def __imul__(a, b):
        if isinstance(b, (float, int, complex)):
            a.x *= b
            a.y *= b
        else:
            a.x *= b.x
            a.y *= b.y
        return a

    def __div__(a, b):
        if isinstance(b, (float, int, complex)):
            return Vec(a.x/b, a.y/b)
        return Vec(a.x/b.x, a.y/b.y)

    def __idiv__(a, b):
        if isinstance(b, (float, int, complex)):
            a.x /= b
            a.y /= b
        else:
            a.x /= b.x
            a.y /= b.y
        return a

    def __truediv__(a, b):
        return a.__div__(b)

    def __str__(self):
        return 'Vec: [%s, %s]' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()
