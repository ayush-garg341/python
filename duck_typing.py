# Duck typing and easier to ask forgiveness then permission (EAFP)
"""
DUCK TYPING :- type system used in dynamic language where the type or the class of an object is 
less important than the method it defines. Using Duck Typing, we do not check types at all. 
Instead, we check for the presence of a given method or attribute.

In duck typing as long as class has implementation of a function, the type of it, does not matter.

Duck typing extends the concept of dynamic typing in Python.
Dynamic typing means that we can change the type of an object later in the code.
"""

x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type of x is now string
print(type(x))


class PyCharm:
    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention chec")
        print("compiling")
        print("running")


class Laptop:
    def code(self, ide):
        ide.execute()


"""
Here type of ide i.e. object type does not matter as long as object has execute method. This is Duck typing.
But in statically typed language like C++ we would have type of object ( argument ) i.e ide in code fn. definition 
and hence we can't pass any type of ide object.
"""

ide = PyCharm()
print(type(ide))
# ide = MyEditor()
# print(type(ide))

lap = Laptop()
lap.code(ide)


class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, flip!")


class Person:
    def quack(self):
        print("I am quacking like a Duck!")

    def fly(self):
        print("I am flapping my arms")


def quack_and_fly(thing):
    # look before you leap LBYL ( Non-pythonic )
    """
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    """

    # EAFP ( pythonic )
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


person = {"name": "Ayush", "age": 26, "job": "programmer"}
# person = {'name':"Ayush", 'age':26}

# LBYL ( non-pythonic )
if "name" in person and "age" in person and "job" in person:
    print("I am {name} and {age} years old. I am a {job}.".format(**person))
else:
    print("Some missing keys")

# EAFP ( pythonic )
try:
    print("I am {name} and {age} years old. I am a {job}.".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))
