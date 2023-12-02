'''
Basic Register class for use in days 18 and 23

@author: Nick DeMasi

'''

class Register(object):
    def __init__(self, val, s):
        self.register = {i: val for i in s}

    def add(self, x, y):
        '''Adds value of y (or at position y) to value at position x'''
        self.register[x] += self.get_value(y)

    def get_value(self, x):
        '''Returns value of x depending on if int or register key'''
        if x in self.register.keys():
            return self.register[x]
        return x

    def mod(self, x, y):
        '''Modulos value at position x by value y (or at position y)'''
        self.register[x] %= self.get_value(y)

    def mul(self, x, y):
        '''Multiplies value at position x by value y (or at position y)'''
        self.register[x] *= self.get_value(y)

    def set(self, x, y):
        '''Updates values in register'''
        self.register[x] = self.get_value(y)

    def sub(self, x, y):
        '''Subtracts from value at position x, value y (or at position y)'''
        self.register[x] -= self.get_value(y)
