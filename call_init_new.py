"""

    __call__():
        A callable object is one which can be called like a function.
        The call method __new__ and __init__ in the same order. First __new__ and then __init__

    __new__():
        __new__ method will be called when an object is created and __init__ method will be called to initialize the object. 
        In the base class "object", the __new__ method is defined as a static method which requires to pass a parameter cls. 
        cls represents the class that is needed to be instantiated.
        
        super(MyClass, cls).__new__(cls, *args, **kwargs) or instance = object.__new__(cls, *args, **kwargs)
        
        If both __init__ method and __new__ method exists in the class, then the __new__ method is executed first and decides whether to use __init__ method or not, 
        because other class constructors can be called by __new__ method or it can simply return other objects as an instance of this class.

    __init__():
        Python constructor. Does not return anything
        it is invoked automatically when an object of the class is defined. 
        It initializes the required members with default values provided.
        
"""

print("------------------------- Call method -------------------------")

class A:
    def __init__(self, x):
        print("inside __init__()")
        self.y = x
  
    def __str__(self):
        print("inside __str__()")
        print("value of y:", str(self.y))
  
    def __call__(self):
        res = 0
        print("inside __call__()")
        print("adding 2 to the value of y")
        res = self.y + 2
        return res


# declaration of instance of class A
a = A(3)
  
# calling __str__() for a
a.__str__()
  
# calling __call__() for a 
r = a()
print(r)
  
# declaration of another instance
# of class A
b = A(10)
  
# calling __str__() for b
b.__str__()
  
# calling __call__() for b
r = b()
print(r)

print()
print("---------------------------- New and init method ------------------------")

class A(object):
    def __new__(cls):
        print("Creating instance")
        print("cls = ",cls)
        print("A = ", A)
        # return super(A, cls).__new__(cls) # works
        return object.__new__(cls)
  
    def __init__(self):
        print("Init is called")
  
A()


class A(object):
    def __new__(cls):
        print("Creating instance")
  
    # It is not called. Since new does not return instance of the class. __new__ controls the __init__ method
    def __init__(self):
        print("Init is called")
  
print(A())

print()
print("----------------------------- New vs init method --------------------------")

class A:
    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)


def how_object_construction_works():
    x = A(1, 2, 3, x=4)

    # above is equivalent to below, but this can be customized using metaclasses

    x = A.__new__(A, 1, 2, 3, x=4)
    if isinstance(x, A):
        print("same type ", type(x))
        type(x).__init__(x, 1, 2, 3, x=4)
    print(x)

how_object_construction_works()


class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)

    # Error: tuples are immutable, even in init
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()


def inheriting_immutable_uppercase_tuple_example():
    print("UPPERCASE TUPLE EXAMPLE")
    print(UppercaseTuple(["hi", "there"]))

inheriting_immutable_uppercase_tuple_example()