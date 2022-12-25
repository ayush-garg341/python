import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # class method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # static methods don't pass anything ( instance or class ) automatically
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Ayush", "Garg", 50000)
emp_2 = Employee("Arnim", "Garg", 60000)

Employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.05)  ---> this is very rare seen in practice

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# constructing instance from emp string
new_emp_1 = "john-doe-70000"
new_emp = Employee.from_string(new_emp_1)

print(new_emp.email)
print(new_emp.pay)


my_date = datetime.date(2021, 10, 22)
print(Employee.is_workday(my_date))
