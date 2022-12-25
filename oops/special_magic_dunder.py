class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Without this special __repr__ dunder method, when we do print(emp_1), it print some vague memory address...
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())


emp_1 = Employee("Ayush", "Garg", 50000)
emp_2 = Employee("Arnim", "Garg", 60000)

print("adding two employees salary => ", emp_1 + emp_2)

print("=================== length =================")
print(len("test"))
print("test".__len__())
print(len(emp_1))


"""
By default __str__ gets executed, but if it is not there __repr__ will get executed.
If not both are present then some vague memory address will get printed.
"""
print(emp_1)

print("====================  calling specific methods  =====================")

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())


print("===================== some built-in method  =======================")
print(int.__add__(1, 2))
print(str.__add__("a", "b"))
