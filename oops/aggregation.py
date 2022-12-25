# Form of association

"""
Aggregation follows the Has-A model. 
This creates a parent-child relationship between two classes, with one class owning the object of another.

In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner.
The owner object could get deleted, but the owned object can continue to exist in the program.
In aggregation, the parent only contains a reference to the child, which removes the child's dependency.
"""


# Each person is associated with a country, but the country can exist without that person.


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person name: ", self.name)
        self.country.printDetails()


c = Country("India", 125000000)
p = Person("Ayush Garg", c)

p.printDetails()

del p

print("After deleting person object, country can still exist")
c.printDetails()
