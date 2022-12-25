"""
    Interface Segregation Principle:
    
    Make fine grained interfaces that are client specific. Clients should not be
    forced to depend upon interfaces that they do not use.  This principle deals
    with the disadvantages of implementing big interfaces.

"""

from abc import ABC, abstractmethod

print(
    "------------------------------------------  Before ISP  ---------------------------------------------"
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

    @abstractmethod
    def auth_sms(
        self,
    ):  # but not every kind of payment will have auth sms, and hence needed ISP
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print("Verifying SMS code {}".format(code))
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_payment_status()


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    # This method we have implemented forcefully, though it's not required and hence violate ISP.
    def auth_sms(self, code):
        raise Exception("Credit card payment don;t support SMS code authorization")

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_payment_status()


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_add):
        self.email_add = email_add
        self.verified = False

    def auth_sms(self, code):
        print("Verifying SMS code {}".format(code))
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address : {self.email_add}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = DebitPaymentProcessor("0123498765")
payment_processor.auth_sms("12345")
payment_processor.pay(order)
print(order.status)


print(
    "------------------------------------------  After ISP  ---------------------------------------------"
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


class PaymentProcessor_SMS(PaymentProcessor):

    """Inheriting pay abstract method from PaymentProcessor class. No need to define it in this class"""

    @abstractmethod
    def auth_sms(self):
        pass


class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print("Verifying SMS code {}".format(code))
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
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


class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email_add):
        self.email_add = email_add
        self.verified = False

    def auth_sms(self, code):
        print("Verifying SMS code {}".format(code))
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address : {self.email_add}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = DebitPaymentProcessor("0123498765")
payment_processor.auth_sms("12345")
payment_processor.pay(order)
print(order.status)


print(
    "------------------------------------------  ISP After composition  ---------------------------------------------"
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


class SMSAuthorizer:
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
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
    def __init__(self, email_add, authorizer: SMSAuthorizer):
        self.email_add = email_add
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address : {self.email_add}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())

authorizer = SMSAuthorizer()
authorizer.verify_code(465839)
payment_processor = DebitPaymentProcessor("0123498765", authorizer)
payment_processor.pay(order)
print(order.status)
