"""
    Liskov Substitution Principle
    A sub-class must be substitutable for its super-class.  The aim of this
    principle is to ascertain that a sub-class can assume the place of its
    super-class without errors.  If the code finds itself checking the type of class
    then, it must have violated this principle.

"""


from abc import ABC, abstractmethod

print(
    "------------------------------------------  Before LSP  ---------------------------------------------"
)


class Order:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.status = "open"

    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i] * self.quantities[i]

        return total

    def set_payment_status(self):
        self.status = "paid"


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_payment_status()


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_payment_status()


class PaypalPaymentProcessor(PaymentProcessor):

    """Here we are abusing variable security_code with email address."""

    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Using email address : {security_code}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = PaypalPaymentProcessor()
payment_processor.pay(order, "gargayush341@gmail.com")
print(order.status)


print(
    "------------------------------------------  After LSP  ---------------------------------------------"
)


class Order:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.status = "open"

    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i] * self.quantities[i]

        return total

    def set_payment_status(self):
        self.status = "paid"


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_payment_status()


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_payment_status()


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_add):
        self.email_add = email_add

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Using email address : {self.email_add}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = PaypalPaymentProcessor("gargayush341@gmail.com")
payment_processor.pay(order)
print(order.status)
