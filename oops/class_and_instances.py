class Employee:

    raise_amount = 1.04 # class variable

    def __init__(self, first, last, pay):
        # all below are instance variables, unique to each instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Ayush", "Garg", 50000) # instance of class. 
emp_2 = Employee("Arnim", "Garg", 60000)

# ========================================== classes and instances ==============================

# print(emp_1.first)
# print(emp_2.first)
# print(emp_1.fullName())
# print(Employee.fullName(emp_1))

# ==========================================  class variables ====================================

print(emp_1.__dict__)
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(Employee.__dict__)
print(emp_2.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


