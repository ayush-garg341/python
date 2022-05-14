"""
Class Method:
    A class method receives the class as an implicit first argument, just like an instance method receives the instance.

    class C(object):
        @classmethod
        def fun(cls, arg1, arg2, ...):
           ....

    - They have the access to the state of the class as it takes a class parameter that points to the class
       and not the object instance.
    - It can modify a class state that would apply across all the instances of the class.
    - We generally use class method to create factory methods. Factory methods return class objects
      ( similar to a constructor ) for different use cases.

Static Method:
    A static method does not receive an implicit first argument.

    class C(object):
        @staticmethod
        def fun(arg1, arg2, ...):
            ...

    - A static method can’t access or modify the class state.
    - A static method is also a method that is bound to the class and not the object of the class.
    - We generally use static methods to create utility functions.
"""

from datetime import date


class Person:
    _entity = "Person"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, year):
        # cls._entity = "Student"
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person("mayank", 21)
print(person1._entity)

person2 = Person.from_birth_year("mayank", 1996)

# Modify class variable
Person._entity = "Student"

print(person2._entity)
print(person1._entity)

print(person1._age)
print(person2._age)

print(Person.is_adult(22))
