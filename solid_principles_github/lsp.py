"""
    Liskov Substitution Principle
    A sub-class must be substitutable for its super-class.  The aim of this
    principle is to ascertain that a sub-class can assume the place of its
    super-class without errors.  If the code finds itself checking the type of class
    then, it must have violated this principle.
    Let's use our Animal example.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "roar"

    def lion_leg_count(self):
        print("Lion has 4 legs")


class Mouse(Animal):
    def make_sound(self):
        return "squeek"

    def mouse_leg_count(self):
        print("Mouse has 3 legs")


class Cat(Animal):
    def make_sound(self):
        return "meow"

    def cat_leg_count(self):
        print("Cat has 4 legs")


animals = [Lion("lion"), Mouse("mouse"), Cat("cat")]


def animal_leg_count(animals):
    for animal in animals:
        if isinstance(animal, Lion):
            animal.lion_leg_count()
        elif isinstance(animal, Mouse):
            animal.mouse_leg_count()
        elif isinstance(animal, Cat):
            animal.cat_leg_count()


animal_leg_count(animals)


"""
    To make this function follow the LSP principle, we will follow this LSP
    requirements postulated by Steve Fenton:
    If the super-class (Animal) has a method that accepts a super-class type
    (Animal) parameter.  Its sub-class(Pigeon) should accept as argument a
    super-class type (Animal type) or sub-class type(Pigeon type).  If the
    super-class returns a super-class type (Animal).  Its sub-class should return a
    super-class type (Animal type) or sub-class type(Pigeon).  Now, we can
    re-implement animal_leg_count function:
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def leg_count(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "roar"

    def leg_count(self):
        print("Lion has 4 legs")


class Mouse(Animal):
    def make_sound(self):
        return "squeek"

    def leg_count(self):
        print("Mouse has 3 legs")


class Cat(Animal):
    def make_sound(self):
        return "meow"

    def leg_count(self):
        print("Cat has 4 legs")


animals = [Lion(), Mouse(), Cat()]


def animal_leg_count(animals):
    for animal in animals:
        print(type(animal), animal.__dict__)
        print(animal.leg_count())


animal_leg_count(animals)
