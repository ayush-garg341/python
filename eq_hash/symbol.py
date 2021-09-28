class Symbol:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        if self.isEpsilon():
            return "e"
        else:
            return str(self.value)

    def isEpsilon(self):
        if self.value == None:
            return True
        else:
            return False


if __name__ == "__main__":
    x = Symbol("NP")
    y = Symbol("NP")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)  # False, compares in-memory address, are they pointing to the same memory location ?
    print(x == y)
    print(len(symbols))

"""
    Every instance of a class or an object is created at different memory address, no matter what the data values are.
    We can check the memory address using id() method.
    "is" method compares the memory address of the objects.

    By Default if we are not overriding "==", it will give us the same result as "is".
    Look above how we override default "==", by first comparing the types of two objects and then their values.

    From Python Docs:
    https://docs.python.org/3/reference/datamodel.html

    If a class does not define an __eq__() method it should not define a __hash__() operation either.
    if it defines __eq__() but not __hash__(), its instances will not be usable as items in hashable collections eg. set, dict. 
    If a class defines mutable objects and implements an __eq__() method, it should not implement __hash__(), 
    since the implementation of hashable collections requires that a key’s hash value is immutable.

    Only immutable objects are considered as hashable and hence valid keys for hashable collection like set, dict

    Try to run the above code with __eq__ and __hash__ method commented.
"""