class Arithmetic(object):
    """A simple example class for demonstation purposes
    """
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return self.addition(a, -b)

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return self.multiplication(a, 1/b)
        else:
            raise ValueError('b is 0. Cannot divide by 0.')