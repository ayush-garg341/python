class Employee:

    num_of_emps = 0  # class variable
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        # all below are instance variables, unique to each instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(
            self.pay * self.raise_amount
        )  # we can access raise_amount using Employee.raise_amount also


print(Employee.num_of_emps)

emp_1 = Employee("Ayush", "Garg", 50000)  # instance of class.
emp_2 = Employee("Arnim", "Garg", 60000)

print(Employee.num_of_emps)

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
print(
    emp_2.raise_amount
)  # raise amount fall back to class variable, since no raise_amount instance var is present.

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
