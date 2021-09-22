class Employee:
    def __init__(self, first, last, pay):
        # all below are instance variables, unique to each instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Ayush", "Garg", 50000) # instance of class. 
emp_2 = Employee("Arnim", "Garg", 60000)

print(emp_1.first)
print(emp_2.first)
print(emp_1.fullName())
print(Employee.fullName(emp_1))