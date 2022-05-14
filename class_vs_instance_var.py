"""
Instance variable:
    If the value of a variable varies from object to object, then such variables are called instance variables.
    Variables that we define inside __init__.

Class Variable:
    A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
    Class variables are shared by all instances of a class.
"""


class Student:
    # Class variable
    school_name = "ABC School "

    # constructor
    def __init__(self, name, roll_no):
        # instance variable
        self.name = name
        self.roll_no = roll_no

        # accessing class vars in constructor
        print("In init : ", self.school_name)
        print("In init : ", Student.school_name)

    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name, self.school_name)

    @staticmethod
    def show_static():
        print("School name in static method is: ", Student.school_name)


# create Object
s1 = Student("Emma", 10)
print("Before")
s1.show()
s1.show_static()

# Modify class variable
Student.school_name = "XYZ School"
print("After")
s1.show()
s1.show_static()
