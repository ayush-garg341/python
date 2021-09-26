"""
An interface is a collection of method signatures that should be provided by the implementing class.
An abstract method is one that the interface simply defines. It doesn't implement the methods. 
This is done by classes, which then implement the interface and give concrete meaning to the interface's abstract methods.


Python interface	                                        |   Python abstract class
------------------------------------------------------------------------------------------------------------------------

1. An interface is a set of methods                         |   We can use an abstract base class to define and enforce an interface. 
and attributes on that object.	

2. All methods of an interface are abstract.              	|   An abstract class can have abstract methods as well as concrete methods.

3. We use an interface if all the features need             |   Abstract classes are used when there is some common feature shared by all 
to be implemented differently for different objects.	        the objects as they are.

4. The interface is slow as compared to the abstract class.	|   Abstract classes are faster.


Two types of interfaces:-
    1. Informal Python interface
    2. Formal Python Interface

"""

# Informal Python Interface

"""
An informal Python interface is a class that defines methods that can be overridden, but there's no strict enforcement.
"""

print()
print("------------------------------------- INFORMAL INTERFACE ---------------------------------")

class InformalParserInterface:

    def load_data_source(self, path, file_name):
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name):
        """Extract text from the currently loaded file."""
        pass



class PdfParser(InformalParserInterface):
    """Extract text from pdfs"""
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text.
           Overrides InformalPythonInterface.load_data_source() 
        """
        pass

    def extract_text(self, full_file_name):
        """Extract text from the currently loaded file.
           Overrides InformalPythonInterface.extract_text() 
        """
        pass


class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text.
           Overrides InformalPythonInterface.load_data_source() 
        """
        pass

    def extract_text_from_emails(self, full_file_path):
        """Extract text from emails.
           Does not override InformalPythonInterface.extract_text() 
        """
        pass

print("Before defining meta class")
print(issubclass(PdfParser, InformalParserInterface))
print(issubclass(EmlParser, InformalParserInterface)) # True, which poses a bit of a problem since it violates the definition of an interface!


"""
Ideally, you would want issubclass(EmlParser, InformalParserInterface) 
to return False when the implementing class doesn’t define all of the interface’s abstract methods. 
"""


# Now check the method resolution order (MRO) of PdfParser and EmlParser.

"""
This tells you the superclasses of the class in question,
as well as the order in which they're searched for executing a method. 
"""

print(PdfParser.__mro__) 
print(EmlParser.__mro__)


# using metaclass

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods in any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass


class PdfParserNew:
    """Extract text from pdfs"""
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text.
           Overrides InformalPythonInterface.load_data_source() 
        """
        pass

    def extract_text(self, full_file_name):
        """Extract text from the currently loaded file.
           Overrides InformalPythonInterface.extract_text() 
        """
        pass


class EmlParserNew:
    """Extract text from an email"""
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text.
           Overrides InformalPythonInterface.load_data_source() 
        """
        pass

    def extract_text_from_emails(self, full_file_path):
        """Extract text from emails.
           A method defined only in EmlParserNew
           Does not override InformalPythonInterface.extract_text() 
        """
        pass

print("After defining meta class")

print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
print(issubclass(EmlParserNew, UpdatedInformalParserInterface))

print(PdfParserNew.__mro__)
print(EmlParserNew.__mro__)


"""
As you can see, UpdatedInformalParserInterface is a superclass of PdfParserNew, but it doesn’t appear in the MRO. 
This unusual behavior is caused by the fact that UpdatedInformalParserInterface is a virtual base class of PdfParserNew.

Virtual base classes use the .__subclasscheck__() dunder method to implicitly 
check if a class is a virtual subclass of the superclass. 
Additionally, virtual base classes don’t appear in the subclass MRO.
"""

# Example

class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))

class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass


"""
Now that the setup for creating virtual base classes is done you’ll define two concrete classes, Employee and Friend. 
The Employee class inherits from PersonSuper, while Friend implicitly inherits from Person
"""

# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

class Friend:
    """Built implicitly from Person.
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass


emp = Employee()

print("More example of virtual class")

print("Employee is a subclass of PersonSuper = {} since inheriting from it".format(issubclass(Employee, PersonSuper)))
print("Person Super is a subclass of Person = {} since it implements all methods of Person".format(issubclass(PersonSuper, Person)))
print(issubclass(Employee, Person))
print("Friend is not inheriting from PersonSuper and no relation of meta class as well and hence = {}".format(issubclass(Friend, PersonSuper)))
print("Person is acting as virtual base class for friend and hence = {}".format(issubclass(Friend, Person)))

print("Friend is an instance of Person = {}".format(isinstance(Friend, Person)))
print("Employee is an instance of PersonSuper = {}".format(isinstance(Employee, PersonSuper)))

print("emp is an instance of Employee = {}".format(isinstance(emp, Employee)))
print("emp is an instance of PersonSuper = {}".format(isinstance(emp, PersonSuper)))


print()
print("--------------------------------- FORMAL INTERFACE ---------------------------")

"""
Informal interfaces can be useful for projects with a small code base and a limited number of programmers. 
However, informal interfaces would be the wrong approach for larger applications. 

To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin ABCMeta from the abc module.
"""

# Example using .__subclasshook__()

import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

    def hello(self):
        print("Hey from eml parser class using subclasshook")

print("----------------------------- using subclasshook -------------------------------")

pdfParser = PdfParserNew()
emlParser = EmlParserNew()
emlParser.hello()

print(issubclass(PdfParserNew, FormalParserInterface)) # True
print(issubclass(EmlParserNew, FormalParserInterface)) # False

# Using abc to register vitual subclass

"""
Once you’ve imported the abc module, you can directly register a virtual subclass by using the .register() metamethod. 
In the next example, you register the interface Double as a virtual base class of the built-in __float__ class:
"""

print("------------------------------ registering the class ------------------------------- ")

class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass

Double.register(float)

print(issubclass(float, Double))
print(isinstance(1.2345, Double))

# you can use it as class decorator to set the decorated class as a virtual subclass
@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double)) 

# Using subclass detection with registration

"""
You must be careful when you’re combining .__subclasshook__() with .register(), as .__subclasshook__() takes precedence over virtual subclass registration. 
To ensure that the registered virtual subclasses are taken into consideration, you must add NotImplemented to the .__subclasshook__() dunder method. 
The FormalParserInterface would be updated to the following:
"""

print("----------------------------- using subclasshook and registering tha class -------------------------------")

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

@FormalParserInterface.register   # try commenting it and then see the output
class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


pdfParser = PdfParserNew()
emlParser = EmlParserNew()

print(issubclass(PdfParserNew, FormalParserInterface)) # True
print(issubclass(EmlParserNew, FormalParserInterface)) # True

"""
Since you’ve used registration, you can see that EmlParserNew is considered a virtual subclass of your FormalParserInterface interface. 
This is not what you wanted since EmlParserNew doesn’t override .extract_text(). 
Please use caution with virtual subclass registration!
"""


# Using abstract method declaration
"""
An abstract method is a method that’s declared by the Python interface, but it may not have a useful implementation. 
The abstract method must be overridden by the concrete class that implements the interface in question.
"""


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


pdfParser = PdfParserNew()
emlParser = EmlParserNew() # will raise the error

"""
Above you’ve finally created a formal interface that will raise errors when the abstract methods aren’t overridden.
"""