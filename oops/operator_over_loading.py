class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp


obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)

"""
    You can name the second argument anything, but as per convention, 
    we will be using the word other to reference the other object.
"""


"""
    Operator	Method
        +	    __add__ (self, other)
        -	    __sub__ (self, other)
        /	    __truediv__ (self, other)
        *	    __mul__ (self, other)
        <	    __lt__ (self, other)
        >	    __gt__ (self, other)
        ==	    __eq__ (self, other)
"""
