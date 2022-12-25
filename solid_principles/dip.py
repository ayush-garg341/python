"""
    Dependency Inversion Principle:

        Dependency should be on abstractions not concretions 
            A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
            B. Abstractions should not depend on details. Details should depend upon abstractions.

        There comes a point in software development where our app will be largely
        composed of modules.  When this happens, we have to clear things up by using
        dependency injection.  High-level components depending on low-level components
        to function.
"""

from abc import abstractmethod, ABC


print(
    "------------------------------------------  Before DIP  ---------------------------------------------"
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


print(
    "------------------------------------------  After DIP  ---------------------------------------------"
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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class SMS_Authorizer(Authorizer):
    def __init__(self) -> None:
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class Google_Authorizer(Authorizer):
    def __init__(self) -> None:
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class Robot_Authorizer(Authorizer):
    def __init__(self) -> None:
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
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
    def __init__(self, email_add, authorizer: Authorizer):
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

# authorizer = SMS_Authorizer()
authorizer = Robot_Authorizer()
# authorizer.verify_code(465839)
authorizer.not_a_robot()
payment_processor = PaypalPaymentProcessor("gargayush341@gmail.com", authorizer)
payment_processor.pay(order)
print(order.status)
