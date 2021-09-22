"""
Let's say the client changed the first name later at some point. Then we need to update the email as well.
But email we are constructing inside constructor that will get called only once when creating object.
So we need to make email as an function that will take the required instance variables and form the email.
But this method have one side, at all the places in client code, we need to change emp_1.email to emp_1.email()
At this point of time property decorator becomes handy.
"""

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property # getter no need to call as a function
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property # getter 
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter # setter
    def fullName(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last  = last

    @fullName.deleter # deleter
    def fullName(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

emp_1 = Employee("Ayush", "Garg", 50000)

print(emp_1.email)

emp_1.first = "AAyush"

print(emp_1.email)
print(emp_1.first)
print(emp_1.fullName)


emp_1.fullName = "AAyush Kumar"
print(emp_1.email)
print(emp_1.first)
print(emp_1.fullName)

del emp_1.fullName
print(" =============   After deleting full name  ============== ")
print(emp_1.first)