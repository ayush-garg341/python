"""
    User classes are considered mutable. Python doesn't have (absolutely) private attributes, 
    so you can always change a class by reaching into the internals.

    For using your class as a key in a dict or storing them in a set, you can define a .__hash__() method and a .__eq__() method, 
    making a promise that your class is immutable. You generally design your class API to not mutate the internal state after creation in such cases.
"""

# For example, if your engines are uniquely defined by their id, you can use that as the basis of your hash:

class Engine(object):
    def __init__(self, id):
        self.id = id

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return NotImplemented

eng1 = Engine(1)
eng2 = Engine(2)

print(eng1 == eng2)
print(eng1 == eng1)
print(eng1 == Engine(1))
engines = set([eng1, eng2])
print(engines)
engines.add(Engine(1))
print(engines)

print(Engine(1) in [eng1, eng2])