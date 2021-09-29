"""
    A class should be closed for modification but open for extension.

    Let's say tomorrow we want to add payment through paypal, then we need to add another fun. paypal_pay()
"""

from abc import ABC, abstractmethod

print("------------------------------------------  Before OCP  ---------------------------------------------")

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



class PaymentProcessor:

    def debit_pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid" # Wrong practice of setting payment status to paid, can call setStatus()

    def credit_pay(self, order,  security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_payment_status()

order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = PaymentProcessor()
payment_processor.credit_pay(order, "09871234")
print(order.status)


print("------------------------------------------  After OCP  ---------------------------------------------")

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

    def pay(self, order,  security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_payment_status()


class PaypalPaymentProcessor(PaymentProcessor):

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
