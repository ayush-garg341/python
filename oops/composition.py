"""
Composition is the practice of accessing other class objects in your class. 
In such a scenario, the class which creates the object of the other class is known as the owner and is responsible for the lifetime of that object.

Composition relationships are Part-of relationships where the part must constitute a segment of the whole object.
In composition, the lifetime of the owned object depends on the lifetime of the owner.
"""

# A car is composed of an engine, tires, and doors.
# In this case, a Car owned these objects, so a Car is an Owner class, and the tires, doors, and engine classes are Owned classes.


class Engine:
    def __init__(self, engine):
        self.capacity = engine

    def printDetails(self):
        print("Engine capacity : ", self.capacity)


class Doors:
    def __init__(self, doors):
        self.doors = doors

    def printDetails(self):
        print("Number of doors : ", self.doors)


class Tires:
    def __init__(self, tires):
        self.tires = tires

    def printDetails(self):
        print("Number of tires : ", self.tires)


class Car:
    def __init__(self, eng, doors, tires, color):
        self.engine = Engine(eng)
        self.doors = Doors(doors)
        self.tires = Tires(tires)
        self.color = color

    def printDetails(self):
        self.engine.printDetails()
        self.doors.printDetails()
        self.tires.printDetails()
        print("Color of car is : ", self.color)


car = Car(1500, 3, 4, "Black")

car.printDetails()
