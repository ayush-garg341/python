from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        """Implement in child class."""


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Defualt Name", 0)

        return PersonSingleton.__instance

    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton can not be instantiated more than once")
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


p1 = PersonSingleton("Ayush Garg", 26)
print(p1)
p1.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()

print(id(p1) == id(p2))

p2 = PersonSingleton("Arnim Garg", 23)
print(p2)
p2.print_data()
