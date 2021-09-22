class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) --> also valid 
        self.prog_lang = prog_lang


class Manager(Employee):

    # why we didn't pass empployees as empty list, but None ?

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if(employees == None):
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
     
    def print_emps(self):
        for emp in self.employees:
            print("----> ", emp.fullName())


dev_1 = Developer("Ayush", "Garg", 50000, 'python')
dev_2 = Developer("Arnim", "Garg", 60000, 'c++')

print(dev_1.email)
print(dev_1.prog_lang)

# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise() # raise amount will get changed to 1.10
print(dev_1.pay)


mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)

print("================= before adding new employe =======================")

mgr_1.print_emps()

mgr_1.add_employee(dev_2)

print("================= after adding new employe =======================")

mgr_1.print_emps()

mgr_1.remove_employee(dev_1)

print("================= after removing first  employe =======================")

mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))