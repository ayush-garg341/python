"""
The term metaprogramming refers to the potential for a program to have knowledge of or manipulate itself. 
Python supports a form of metaprogramming for classes called metaclasses.

Meta classes are used when we want to impose restriction/rules on how classes should be define, what attribute they should have, 
then we can make use of meta classes.
"""


# python 2

# class and type are not quite the same thing.
# If obj is an instance of an old-style class, obj.__class__ designates the class, but type(obj) is always instance.

"""
class Foo:
    pass

x = Foo()
print(x.__class__) # <class __main__.Foo at 0x000000000535CC48>
print(type(x)) # <type 'instance'>

"""

# python 3

# If obj is an instance of a new-style class, type(obj) is the same as obj.__class__

class Foo:
    pass

x = Foo()
print(x.__class__) # <class '__main__.Foo'>
print(type(x)) # <class '__main__.Foo'>
print(type(x) is x.__class__) # True


n = 5
d = {'a':1, 'b':2}

for obj in (n, d, x):
    print(type(obj) is obj.__class__)


# In python everything is an object. Classes are objects as well. As a result, a class must have a type. 
# In general, the type of any new-style class is type.

print("type of Foo is ",type(Foo)) # <class 'type'>

for t in (int, float, dict, list, tuple):
    print("type of {} is {}".format(t, type(t)))

print("type of type is ", type(type)) # <class 'type'>


"""
type is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, 
any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass.
"""

"""
You can also call type() with three arguments — type(<name>, <bases>, <dct>):

    1. <name> specifies the class name. This becomes the __name__ attribute of the class.
    2. <bases> specifies a tuple of the base classes from which the class inherits. 
        This becomes the __bases__ attribute of the class.
    3. <dct> specifies a namespace dictionary containing definitions for the class body. 
        This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

"""


# Example 1

Foo = type('Foo', (), {})
x = Foo()
print(x) 
# <__main__.Foo object at 0x04CFAD50>



class Foo:
    pass
x = Foo()
print(x)

# <__main__.Foo object at 0x04CFAD50>



# Example 2
# Here, <bases> is a tuple with a single element Foo, specifying the parent class that Bar inherits from

Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
print("Creating class using type")
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)

class Bar(Foo):
    attr = 100

x = Bar()
print("Creating class using normal convention")
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


# Example 3
# This time, <bases> is again empty. Two objects are placed into the namespace dictionary via the <dct> argument.

Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': lambda x : x.attr
    }
)

print("=========== type =========== ")
x = Foo()
print(x.attr)
print(x.attr_val())


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr

print("==============  Normal ============== ")
x = Foo()
print(x.attr)
print(x.attr_val())


# Example 4
# Only very simple functions can be defined with lambda in Python.

def f(obj):
    print("attr = ", obj.attr)

Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': f
    }
)

print("=========== type =========== ")
x = Foo()
print(x.attr)
x.attr_val()



class Foo:
    attr = 100
    attr_val = f

print("==============  Normal ============== ")
x = Foo()
print(x.attr)
x.attr_val()


# Custom Meta class

print("Custom meta class")

"""
    class Foo:
        pass
    f = Foo()

    The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:
        1. The __call__() method of Foo’s parent class is called. 
            Since Foo is a standard new-style class, its parent class is the type metaclass, so type's __call__() method is invoked.
        2. That __call__() method in turn invokes the following:
            a. __new__()
            b. __init__()

    If Foo does not define __new__() and __init__(), default methods are inherited from Foo’s ancestry. 
    But if Foo does define these methods, they override those from the ancestry, which allows for customized behavior when instantiating Foo.

    type.__new__ = new -->> will give error
    You can’t reassign the __new__() method of the type metaclass. Python doesn’t allow it.
    type is the metaclass from which all new-style classes are derived. You really shouldn’t be mucking around with it anyway
"""


class Meta(type):

    """
        See how we are changing and controlling the attrs of class using meta class..
        Metaclasses are sometimes referred to as class factories.
    """

    def __new__(self, class_name, bases, attrs):

        print("Self = ", self)
        print("Class name = ", class_name)
        print("Bases = ", bases)
        print("before imposing restriction attrs = ", attrs)

        a = {}

        for name, val in attrs.items():
            if(name.startswith("__")):
                a[name] = val
            else:
                a[name.upper()] = val

        print("after imposing restriction attrs = ", a)

        # return type(class_name, bases, a) # this is also correct
        return super().__new__(self, class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 10

    def hello(self):
        print("Hiiiiii")

d = Dog()
d.HELLO()


print("========== Class Decorator ============ ")


def decorator(cls):
    class NewClass(cls):
        attr = 100

        def hello():
            print("Helloo from decorator class")

    return NewClass

@decorator
class X:
    pass

@decorator
class Y:
    pass

@decorator
class Z:
    pass

print(X.attr)
X.hello()
print(Y.attr)
Y.hello()
print(Z.attr)
Z.hello()