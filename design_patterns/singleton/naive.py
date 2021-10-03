"""
    It’s pretty easy to implement a sloppy Singleton. 
    You just need to hide the constructor and implement a static creation method.

    The same class behaves incorrectly in a multithreaded environment. 
    Multiple threads can call the creation method simultaneously and get several instances of Singleton class.
"""

class SingletonMeta(type):
    
    """
        The Singleton class can be implemented in different ways in Python. Some
        possible methods include: base class, decorator, metaclass. We will use the
        metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwds):

        print("cls = ", cls)
        print("args = ", args)
        print("kwds = ", kwds)

        """
            Possible changes to the value of the `__init__` argument do not affect
            the returned instance.
        """

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance        
        return cls._instances[cls]

    

class Singleton(metaclass=SingletonMeta):
    
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


# s1 = Singleton()
# s2 = Singleton()

# print(id(s1) == id(s2))


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")