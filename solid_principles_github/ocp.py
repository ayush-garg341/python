"""
    Open-Closed Principle
    Software entities(Classes, modules, functions) should be open for extension, not
    modification.

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass


animals = [Animal("lion"), Animal("mouse")]


def animal_sound(animals):
    for animal in animals:
        if animal.name == "lion":
            print("Roar")

        elif animal.name == "mouse":
            print("Squeek")


animal_sound(animals)


"""
    The function animal_sound does not conform to the open-closed principle because
    it cannot be closed against new kinds of animals.  If we add a new animal,
    Snake, We have to modify the animal_sound function.  You see, for every new
    animal, a new logic is added to the animal_sound function.  This is quite a
    simple example. When your application grows and becomes complex, you will see
    that the if statement would be repeated over and over again in the animal_sound
    function each time a new animal is added, all over the application.
"""

print("----------------------------------------")

animals = [Animal("lion"), Animal("mouse"), Animal("cat")]


def animal_sound(animals):
    for animal in animals:
        if animal.name == "lion":
            print("Roar")

        elif animal.name == "mouse":
            print("Squeek")

        elif animal.name == "cat":
            print("meow")


animal_sound(animals)


print("----------------------------------------")

"""
    How do we make it (the animal_sound) conform to OCP?
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


class Mouse(Animal):
    def make_sound(self):
        return "squeek"


class Cat(Animal):
    def make_sound(self):
        return "meow"


animals = [Lion("lion"), Mouse("mouse"), Cat("cat")]


def animal_sound(animals):
    for animal in animals:
        print(animal.get_name())
        print(animal.make_sound())


animal_sound(animals)


"""
    Another example:
    Let's imagine you have a store, and you give a discount of 20% to your favorite
    customers using this class: When you decide to offer double the 20% discount to
    VIP customers. You may modify the class like this:
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == "fav":
            return self.price * 0.2
        if self.customer == "vip":
            return self.price * 0.4


"""
    No, this fails the OCP principle. OCP forbids it. If we want to give a new
    percent discount maybe, to a diff.  type of customers, you will see that a new
    logic will be added.
    To make it follow the OCP principle, we will add a new class that will extend
    the Discount.  In this new class, we would implement its new behavior:
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


"""
If you decide 80% discount to super VIP customers, it should be like this:
You see, extension without modification.
"""

# multi-level inheritance, it should be avoided.
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
